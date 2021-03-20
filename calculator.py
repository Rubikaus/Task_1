answer = 0
str = input("Введите первое число: ")
answer = int(str)
while(True):
    str = ''
    str = input("Введите символ и число или '=': ")
    if (str.find('+') >= 0):
        str = str.replace(' ', '')
        str = str.replace('+', '')
        answer += int(str)
    elif (str.find('-') >= 0):
        str = str.replace(' ', '')
        str = str.replace('-', '')
        answer -= int(str)
    elif (str.find('*') >= 0):
        str = str.replace(' ', '')
        str = str.replace('*', '')
        answer *= int(str)
    elif (str.find('/') >= 0):
        str = str.replace(' ', '')
        str = str.replace('/', '')
        answer /= int(str)
    elif (str.find('**') >= 0):
        str = str.replace(' ', '')
        str = str.replace('**', '')
        answer **= int(str)
    elif(str.find('=') >= 0):
        print(answer)
        exit(0)
