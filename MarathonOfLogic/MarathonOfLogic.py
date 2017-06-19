from random import randrange

class ThreeNPlus1:

	bkp_number = 0
	final_number = 0
	# 0 == PAIR | 1 == ODD
	ctrl_counts = {0: 0, 1: 0}

	def random_number(self, start=1):
		return (randrange(start, randrange((start * 3 * 1000000000) + 1 )))

	def check_number(self, number):
		return (number % 2)

	def exec_operation(self):
		number = self.random_number()
		bkp_number = number
		while number > 1:
			mod = self.check_number(number)
			if mod == 0:
				number = (number / 2)
			else:
				number = (number * 3) + 1
			self.increment_count_operation(mod)
		final_number = number
		self.print_result(bkp_number, final_number)

	def increment_count_operation(self, cod_operation):
		value = self.ctrl_counts.get(cod_operation)
		self.ctrl_counts[cod_operation] = value +1
		print('INCREMETING COUNT | KEY: {} - VALUE: {} '.format(cod_operation, self.ctrl_counts.get(cod_operation)))

	def print_result(self, number, final_number):
		print('\n')
		print('##############################################################')
		print('EXTRACTED NUMBER IS: {} '.format(number))
		print('-----------------------------------------')
		print('COUNT PAIR: {} - COUNT ODD: {} '.format(self.ctrl_counts.get(0), self.ctrl_counts.get(1)))
		print('RESULT COUNT OPERATIONS - (PAIR: {} + ODD: {}) == {}'.format(self.ctrl_counts.get(0), self.ctrl_counts.get(1), 
			(self.ctrl_counts.get(0) + self.ctrl_counts.get(1)) ))
		print('##############################################################')
		print('RESULT FINAL NUMBER: {} '.format(final_number))
		print('\n')


if __name__ == '__main__':
	run = ThreeNPlus1()
	run.exec_operation()
