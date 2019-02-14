import unittest
import utils

class Test ( unittest . TestCase ):
    def test_fact ( self ):
        self.assertEqual(utils.fact(1),1)
        with self.assertRaises(ValueError):
            utils.fact(-2)
        self.assertEqual ( utils . fact (0) , 1)

    def test_roots (self):
        self.assertEqual (utils.roots (1,3,-4), (1.0,-4.0))
        self.assertEqual (utils.roots (2,0,0), (0.0,))

    def test_integrate ( self):
        self.assertEqual (utils.integrate ('x ** 2 - 1', -1, 1), 2)
        self.assertEqual (utils.integrate ('x ** 2 - 5', -9, 1), 2)

suite = unittest . TestLoader () . loadTestsFromTestCase ( Test )
runner = unittest . TextTestRunner ()
print ( runner . run( suite ))