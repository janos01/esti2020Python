import triangle
import unittest

class TestTriangel(unittest.TestCase):
	
	def testCalcArea(self):
		self.assertEqual(
			triangle.calcArea(100, 105),
			5250.0, 'Az elvárt érték 5250.0')

	def testCalcAreaZeroOrNegative(self):
		self.assertEqual(
			triangle.calcArea(0, 105),
			-1, 'Az elvárt érték -1')


if __name__== "__main__":
	unittest.main()
