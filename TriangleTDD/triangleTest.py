from triangle import Triangle
import unittest

class TestTriangle(unittest.TestCase):
	
	def testCalcArea(self):
		area = Triangle.calcArea(100, 105)
		self.assertEqual(area, 5250.0, 
		'Az elvárt érték 5250.0')
		
	def testCalcArea2(self):
		area = Triangle.calcArea(200, 250)
		self.assertEqual(area, 25000.0, 
		'Az elvárt érték 25000.0')

	def testCalcAreaZeroOrNegative(self):
		area = Triangle.calcArea(0, 250)
		self.assertEqual(area, -1, 
		'Az elvárt érték -1')

	def testCalcAreaZeroOrNegative2(self):
		area = Triangle.calcArea(100, 0)
		self.assertEqual(area, -1, 
		'Az elvárt érték -1')


	
if __name__ == "__main__":
	unittest.main()
