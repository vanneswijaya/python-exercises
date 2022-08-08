import time

print ('TIMER')
print ('---------')
print ('Units : ')
print ('1 = Second')
print ('2 = Minute')
print ('3 = Hour')
unit = int(input ('Insert unit (1/2/3) : '))
fill = int(input ('Insert time (in chosen unit) : '))
if unit == 1:
    time.sleep (fill)
elif unit == 2:
    time.sleep (fill*60)
else:
    time.sleep (fill*3600)

print ('DONE')
print ('Bye!')
    
        


