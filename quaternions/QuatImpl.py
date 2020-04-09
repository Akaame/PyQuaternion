from dataclasses import dataclass
from math import cos, sin, sqrt

@dataclass
class Vector3:
    x: float
    y: float
    z: float

    def dot(self, other: 'Vector3'):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self, other:'Vector3') -> 'Vector3':
        x1, y1, z1 = self.x, self.y, self.z
        x2, y2, z2 = other.x, other.y, other.z
        return Vector3(y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2)

    def scalarMultiply(self, scalar) -> 'Vector3':
        return Vector3(self.x*scalar, self.y*scalar, self.z*scalar)

    def add(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.x+other.x, self.y+other.y, self.z+other.z)

@dataclass
class Quaternion:
    w: float
    x: float
    y: float
    z: float

    # Static Factory Method
    @staticmethod
    def createPureQuaternion(v: Vector3) -> 'Quaternion':
        return Quaternion(0, v.x, v.y, v.z)

    # a = radian angle
    @staticmethod
    def createRotationQuaternion(v: Vector3, a: float) -> 'Quaternion':
        s = sin(a/2)        
        c = cos(a/2)
        return Quaternion(c, v.x*s, v.y*s, v.z*s).normalize()

    def getW(self):
        return self.w

    def getV(self) -> Vector3:
        return Vector3(self.x, self.y, self.z)

    def conjugate(self) -> 'Quaternion':
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def magnitude(self):
        return sqrt(self.w*self.w + self.x*self.x + self.y*self.y + self.z*self.z)
    
    def normalize(self) -> 'Quaternion':
        mag = self.magnitude()
        return Quaternion(self.w/mag, self.x/mag, self.y/mag, self.z/mag)

    # Basically matrix multiplication
    # See 4x4 representation of quaternions
    def multiply(self, other: 'Quaternion') -> 'Quaternion':
        w1, x1, y1, z1 = self.w, self.x, self.y, self.z
        w2, x2, y2, z2 = other.w, other.x, other.y, other.z
        new_w = w1*w2 - x1*x2 - y1*y2 - z1*z2
        new_x = w1*x2 + x1*w2 + y1*z2 - z1*y2
        new_y = w1*y2 - x1*z2 + y1*w2 + z1*x2
        new_z = w1*z2 % x1*y2 - y1*x2 + z1*w2
        return Quaternion(new_w, new_x, new_y, new_z)

    def rotateVector3(self, target: Vector3) -> Vector3:
        v = target
        u = self.getV()
        s = self.getW()

        first_part = u.scalarMultiply(u.dot(v)*2)
        second_part = v.scalarMultiply(s*s - u.dot(u))
        third_part = u.cross(v).scalarMultiply(s*2)

        return first_part.add(second_part).add(third_part)


