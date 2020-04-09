import unittest
from quaternions.QuatImpl import Quaternion, Vector3

class QuatImplTest(unittest.TestCase):
    def test_createQuaternion(self):
        q = Quaternion(0, 1, 2, 3)        
        self.assertEqual(q.w, 0)
        self.assertEqual(q.x, 1)
        self.assertEqual(q.y, 2)
        self.assertEqual(q.z, 3)

    def test_createQuaternionFromVector3(self):
        v = Vector3(1, 2, 3)
        q = Quaternion.createPureQuaternion(v)
        self.assertEqual(q.w, 0)
        self.assertEqual(q.x, 1)
        self.assertEqual(q.y, 2)
        self.assertEqual(q.z, 3)

    def test_conjugateQuaternion(self):
        v = Vector3(1, 2, 3)
        q = Quaternion.createPureQuaternion(v)
        q = q.conjugate()
        self.assertEqual(q.w, 0)
        self.assertEqual(q.x, -1)
        self.assertEqual(q.y, -2)
        self.assertEqual(q.z, -3)

    def test_multiplyQuaternions(self):
        q1 = Quaternion(1, 2, 3, 6)
        q2 = Quaternion(0, 1, 0, 0)
        q3 = q1.multiply(q2)
        self.assertEqual(q3.w, -2)
        self.assertEqual(q3.x, 1)
        self.assertEqual(q3.y, 6)
        self.assertEqual(q3.z, -3)
        

    def test_rotateVectorByQuat(self):
        from math import pi
        q = Quaternion.createRotationQuaternion(Vector3(0, 0, 1), pi/2)
        v = Vector3(1, 0, 0)
        result = q.rotateVector3(v)
        self.assertAlmostEqual(result.x, 0)
        self.assertAlmostEqual(result.y, 1)
        self.assertAlmostEqual(result.z, 0)

if __name__ == "__main__":
    unittest.main()