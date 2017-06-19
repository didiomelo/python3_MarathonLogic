from datetime import datetime
from random import randrange

class A:

	count = randrange(1, 10)

	def method_a(self, x, y):
		print('METHOD_A DATA ARE: {} and {} '.format(x, y))
		return (x + y)

class B:

	def call_method_b(self, start=1):
		print('THE COUNT NUMBER IS: {} '.format(A.count))
		while A.count >= 1:
			print('RESULT IS: {} '.format(A.method_a(self, start, randrange(start, randrange((start * 3 * 1000000000) + 1 )))))
			A.count = (A.count -1)

b = B()
b.call_method_b()