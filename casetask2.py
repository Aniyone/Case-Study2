import datetime

d = 0
m = 0
y = 0
print('введите последовательно числами: ')
while ((d > 31) or (d <= 0)):
    d = int(input('день вашего рождения - '))

while ((m > 12) or (m <= 0)):
    m = int(input('месяц вашего рождения - '))
    if (d > 29) and (m == 2):
        print('Error: не может быть более 29 дней в феврале.')
        exit()

while (y <= 0):
    y = int(input('год вашего рождения - '))

#Функция для определения високосного года
def isleapyear(a):
    if (a % 4 != 0):
        leap = False
    elif (a % 100 != 0):
        leap = True
    elif (a % 400 != 0):
        leap = False
    else:
        leap = True
    return leap

#Проверка существует ли введенная дата рождения в рамках григорианского календаря
if (d == 29) and (m == 2) and (isleapyear(y) == False):
    print('Error: год не високосный, невозможно иметь такую дату рождения')
    exit()

#Функция для определения дня недели
def getdayoftheweek(a, b, c):
    dayweeknumber = datetime.date(a, b, c).weekday()
    week = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
    return week[dayweeknumber]

#Функция для вычисления возраста
def getage(a, b, c):
    birthdate = datetime.date(a, b, c)
    currentdt = datetime.datetime.now()
    age = currentdt.year - birthdate.year
    if birthdate.month >= currentdt.month:
        if birthdate.day > currentdt.day:
            age -= 1
    return age

#Цифры в формате электронного табло
numbers = {
    '0': [
        "*****",
        "*   *",
        "*   *",
        "*   *",
        "*****"
    ],
    '1': [
        "  *  ",
        " **  ",
        "  *  ",
        "  *  ",
        " *** "
    ],
    '2': [
        "*****",
        "    *",
        "*****",
        "*    ",
        "*****"
    ],
    '3': [
        "*****",
        "    *",
        "*****",
        "    *",
        "*****"
    ],
    '4': [
        "*   *",
        "*   *",
        "*****",
        "    *",
        "    *"
    ],
    '5': [
        " *** ",
        "*    ",
        " *** ",
        "    *",
        " *** "
    ],
    '6': [
        " *** ",
        "*    ",
        " *** ",
        "*   *",
        " *** "
    ],
    '7': [
        " *** ",
        "    *",
        "    *",
        "    *",
        "    *"
    ],
    '8': [
        " *** ",
        "*   *",
        " *** ",
        "*   *",
        " *** "
    ],
    '9': [
        " *** ",
        "*   *",
        " *** ",
        "    *",
        " *** "
    ],
    ' ': [
        "     ",
        "     ",
        "     ",
        "     ",
        "     "
    ]
} 

#Распределение цифр в выводимые строки и результат вывода
dateofbirth = str(d) + ' ' + str(m) + ' ' + str(y)
lines = ['' for x in range(5)]
for char in dateofbirth:
    for i in range(5):
        lines[i] += numbers[char][i] + '  '
for line in lines:
    print(line)


print(f'{d}/{m}/{y}')
print(getdayoftheweek(y, m, d))
print(f'Високосный год - {isleapyear(y)}')
print(f'Возраст: {getage(y, m, d)}')