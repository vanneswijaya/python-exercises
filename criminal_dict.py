import time

criminals = []

john = {}

john["age"] = 25
john["fullname"] = "John Smith"
john["crime"] = "First Degree Murder"

criminals.append(john)

bill = {}

bill["age"] = 30
bill["fullname"] = "Billy Brock"
bill["crime"] = "Stealing"

criminals.append(bill)

Ethan = {}

Ethan["age"] = 20
Ethan["fullname"] = "Ethan Travis"
Ethan["crime"] = "Drug Dealing"

criminals.append(Ethan)

Raymond = {}

Raymond["age"] = 40
Raymond["fullname"] = "Raymond Chris"
Raymond["crime"] = "Second Degree Murder"

criminals.append(Raymond)

wanna = 'a'

#password = 191919

while wanna != '191919':
	wanna = input ('Password? ')

print ('--------------------')
print ('FBI MOST WANTED LIST')
print ('--------------------')
print ('')
time.sleep (3)
counter = 0
while counter < 3:
	for x in range (0,4):  
		b = "Loading data " + "." * x
		print (b)
		time.sleep(0.5)
	counter += 1
print ('')
print (len(criminals) , 'IDENTIFIED.')
print ('')
time.sleep (3)
for x in criminals:
	age = x["age"]
	fullname = x["fullname"]
	crime = x["crime"]
	print ('Name	: ' + fullname)
	print ('Age 	: ' + str(age))
	print ('Crime	: ' + crime)
	print ('')
	


