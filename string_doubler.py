def string_doubler(str):
    y = ''
    for x in str:
        y += x*2
    print (y)

ask = input('Enter text: ')
string_doubler(ask)
