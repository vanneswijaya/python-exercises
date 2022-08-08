a = list(range(1,100))
print(a)
print('')
total = 0
c = []
for b in a:
    if b % 3 == 0 or b % 5 == 0:
        c.append (b)
        total += b
print (c)
print ('')
print (total)

