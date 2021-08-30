from random import randrange

tortoise_moves = {'fast plod' : 3, 'slip' : -6, 'slow plod' : 1}
hare_moves = {'sleep' : 0, 'big hop' : 9, 'big slip' : -12, 'small hop' : 1, 'small slip' : -2}


tortoise_position = 0
hare_position = 0 

winner = False

while not winner:

	x = randrange(1, 11)
	y = randrange(1, 11)

	if x in range(1, 6):
		tortoise_position += tortoise_moves['fast plod']
	elif x in range(6, 8):
		tortoise_position += tortoise_moves['slip']
	else:
		tortoise_position += tortoise_moves['slow plod']


	if y in range(1, 3):
		hare_position += hare_moves['sleep']
	elif y in range(3, 5):
		hare_position += hare_moves['big hop']
	elif y == 5:
		hare_position += hare_moves['big slip']
	elif y in range(6, 9):
		hare_position += hare_moves['small hop']
	else:
		hare_position += hare_moves['small slip']

	
	if tortoise_position < 0:
		tortoise_position = 0

	if hare_position < 0:
		hare_position = 0


	if hare_position == tortoise_position == 70:
		print("It's a tie!")
		winner = True
	elif hare_position == tortoise_position:
		print(" " * (hare_position - 1), "Ouch!")
	else: 
		print(' ' * (tortoise_position - 1), 'T')
		print(' ' * (hare_position - 1), 'H')

	print('_' * 70)

	if tortoise_position >= 70:
		print('TORTOISE WINS!!! YAY!!!')
		winner = True
	if hare_position >= 70:
		print('Hare wins. Yuch')
		winner = True