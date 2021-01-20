import triangle

def testCalcArea():
	assert triangle.calcArea(100, 105) == 5250.0, 'Az elvárt eredmény: 5250.0'
	assert triangle.calcArea(200, 250) == 25000.0, 'Az elvárt eredmény: 25000.0'

def testCalcAreaZeroOrNegative():
	assert triangle.calcArea(0, 105) == -1, 'Az elvárt eredmény: -1'


testCalcArea()
print('ok testCalcArea')
testCalcAreaZeroOrNegative()
print('ok testCalcAreaZeroOrNegative')
