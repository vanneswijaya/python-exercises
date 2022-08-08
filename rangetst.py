for x in range(6,0,-1):
    print (x)
f1 = [x**2 for x in range(6,0,-1)]
print(f1)

list2 = [1,3,4,1,3]
list3 = []
set1 = set()
total = 0
for x in list2:
    set1.add(x)
for x in set1:
    list3.append(x)
for x in list3:
    total += x
print (total)