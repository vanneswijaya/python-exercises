#f(x) = (x*2) + 5
def math_func1(x):
    a = (x*2) + 5
    return a

def ask_input():
    ask = int(input('Enter a number: '))
    return ask

y = ask_input()
print(math_func1(y))
