import random

chars = ""
charsZag = "ABCDIFGHIJKLMNOPQRSTUVWXYZ"  # переменная с заглавными буквами
charsStr = "abcdifghijklmnopqrstuvwxyz"  # переменная с строчными буквами
charsSpec = "+-/*!&$#&=@<>"  # переменная с спец символами
charsNumber = "1234567890"  # переменная с цифрами

print("[1] - Да, [2] - Нет")
print()
ZagBuk = int(input("Заглавные буквы: "))
StrBuk = int(input("Строчные буквы: "))
SpecSim = int(input("Специальные символы: "))
Number = int(input("Цифры: "))
print()
amout = int(input('Кол-во паролей: '))
lengt = int(input('Длина пароля: '))

if ZagBuk == 1:
    chars = chars + charsZag
if StrBuk == 1:
    chars = chars + charsStr
if SpecSim == 1:
    chars = chars + charsSpec
if Number == 1:
    chars = chars + charsNumber
# создаем цикл который будет повторяться столько, сколько паролей мы ввели
for x in range(amout):
    password = ""
    for i in range(lengt):
        password += random.choice(chars)
    file = open("Пароли.txt", "a")
    file.write(password + '\n')
    file.close()
print('Пароли созданы!')
