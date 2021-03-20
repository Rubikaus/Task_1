try:
    number = int(input("Введите число для проверки: "))
except ValueError:
    print("Вы написали не число")
    exit(0)
remainder = False
if (number == 1):
    print("Число не простое")
    exit(0)
for i in range(2, number):
    if (number % i != 0):
        remainder = False
    else:
        remainder = True
        break
if (remainder == False):
    print("Число простое")
else:
    print("Число не простое")
