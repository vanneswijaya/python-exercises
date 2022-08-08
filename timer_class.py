import time

class Timer():
    def __init__(self, state, time):
        self.state = state
        self.time = time
        
    
    def startTimer(self):
        while True:
            if self.state == "detik":
                time.sleep (self.time)
                print ('DONE')
                break
            if self.state == "menit":
                time.sleep (self.time*60)
                print ('DONE')
                break
            else:
                time.sleep(self.time*3600)
                print ("DONE")
                break

wanna = input ('Do you wanna use timer? (y/n) ')

while wanna == 'y':
    print ('TIMER')
    print ('---------')
    print ('Units : ')
    print ('detik = Second')
    print ('menit = Minute')
    print ('jam = Hour')
    state = int(input ('Insert unit (1/2/3) : '))
    fill = int(input ('Insert time (in chosen unit) : '))
    timer = Timer(state,fill)
    timer.startTimer()
    break