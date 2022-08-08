#input0 = 'vannes'

def ask_name():
    global input0
    #input0 = input('What is ur name: ')
    input0 = 'vannes'
    return input0

def ask_data():
    input1 = int(input('Enter your working hours: '))
    input2 = int(input('Enter your rate per hour: '))
    return input1, input2

def compute_pay(x, y):
    if x > 40:
        return x*y+500
    else:
        return x*y

def run():
    print ('SALARY COMPUTATION FOR EMPLOYEES')
    print ('-------------')
    name = ask_name()
    hour, rate = ask_data()
    pay = compute_pay(hour, rate)
    print (f'Hey {name}, your salary is {pay}')

#ask_name()
run()


