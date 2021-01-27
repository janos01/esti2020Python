class Triangle:
	def calcArea(base, height):
		if base <= 0 or height <= 0:
			return -1
		else:
			return (base*height)/2
