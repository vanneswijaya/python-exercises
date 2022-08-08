total = 0.0
totalcount = 0
numlist = []

while True:
    try:
        numinp = input('Enter a number: ')
        if numinp == 'done':
            break
        numinp = float(numinp)
    except ValueError:
        print ('Invalid input')
        continue
    numlist.append (numinp)
    total += numinp
    totalcount += 1

print ('Total : ' + str(total))
print ('Count : ' + str(totalcount))
print ('Average : ' + str(total/totalcount))
print ('Maximum : ' + str(max(numlist)))
print ('Minimum : ' + str(min(numlist)))



