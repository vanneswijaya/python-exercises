import random

class Game:
	#ATTRIBUTES
	def __init__(self, answer, min, max):
		self.answer = answer
		self.min = min
		self.max = max

	#METHODS
	def get_guess(self):
		ask = input(f'Guess the number! ({self.min}-{self.max})! ')
		if self.is_valid(ask):
			return int(ask)
		else:
			print('Invalid Input')
			return self.get_guess()

	def is_valid(self, num):
		try:
			number = int(num)
		except:
			return False
		return self.min <= number <= self.max

	def play(self):
		count = 0
		while True:
			count += 1
			guess = self.get_guess()
			if guess > self.answer:
				print ('Too big')
			elif guess < self.answer:
				print ('Too small')
			else:
				break

		print (f'Well done! {count} attempts!')

game1 = Game(5, 1, 9)
game2 = Game(random.randint(1,51), 1, 50)
game2.play()