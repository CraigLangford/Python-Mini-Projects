import unittest
from vector import Vector

class TestVector(unittest.TestCase):

    def test_initializes_correctly(self):
        v = Vector(1,3)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 3)
        
        v2 = Vector()
        self.assertEqual(v2.x, 0)
        self.assertEqual(v2.y, 0)

    def test_repr(self):
        v = Vector(2,4)
        self.assertEqual(repr(v), 'Vector(2, 4)')
        self.assertEqual(repr(Vector('2', 3)), 'Vector(\'2\', 3)')
        self.assertEqual(str(v), 'Vector(2, 4)')

    def test_abs(self):
        v = Vector(4, 3)
        self.assertEqual(abs(v), 5)

    def test_bool(self):
        self.assertTrue(Vector(3,2))
        self.assertFalse(Vector(0,0))
        self.assertTrue(Vector(-10,0))

    def test_add(self):
        v = Vector(1,1)+Vector(3,1)
        self.assertEqual(v.x, 4)
        self.assertEqual(v.y, 2)

    def test_multiply(self):
        v = Vector(-3, 8) * 5
        self.assertEqual(v.x, -15)
        self.assertEqual(v.y, 40)

if __name__ == '__main__':
    unittest.main()
