import random

print ('DICE ROLL SIMULATOR')
print ('-------------------')

while True:
	wanna = input ('Wanna roll? (y/n) ')
	if wanna.lower().strip() == 'y':
		print ('You have rolled :', random.randint(1,6))
		break
	elif wanna.lower().strip() == 'n':
		break
	else:
		continue

print ('Bye!')

