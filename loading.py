import time

counter = 0

print ('THIS IS A GAME')

while counter < 3:
	for x in range (0,4):  
		b = "Loading" + "." * x
		print (b)
		time.sleep(0.3)
	counter += 1
print ('Welcome to the game!')

