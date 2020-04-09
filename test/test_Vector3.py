import unittest
from quaternions.QuatImpl import Vector3

class TestVector3(unittest.TestCase):
    def test_createVector3(self):
        v = Vector3(1, 2, 3)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.z, 3)

    def test_addition(self):
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(5, 6, 7)
        result = v1.add(v2)
        self.assertEqual(result.x, 6)        
        self.assertEqual(result.y, 8)
        self.assertEqual(result.z, 10)

    def test_negation(self):
        v1 = Vector3(5, 6, 7)
        result = v1.scalarMultiply(-1)
        self.assertEqual(result.x, -5)        
        self.assertEqual(result.y, -6)
        self.assertEqual(result.z, -7)

    def test_dotProduct(self):
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(5, 6, 7)
        result = v1.dot(v2)
        self.assertEqual(result, 38)    

    def test_crossProduct(self):
        v1 = Vector3(1, 1, -3)
        v2 = Vector3(-1, 3, -1)
        result = v1.cross(v2)
        self.assertEqual(result.x, 8)
        self.assertEqual(result.y, 4)
        self.assertEqual(result.z, 4)

    def test_scalarMultiplication(self):
        v1 = Vector3(1, 2, 3)
        result = v1.scalarMultiply(5)
        self.assertEqual(result.x, 5)        
        self.assertEqual(result.y, 10)
        self.assertEqual(result.z, 15)
    
if __name__ == '__main__':
    unittest.main()