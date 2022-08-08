givenlist = [7,5,4,4,3,1,-2,-3,-5,-7]
total = 0
i = 0
while i < len(givenlist):
    if givenlist[i] <= 0:
        total += givenlist[i]
    else:
        pass
    i += 1
print (total)
