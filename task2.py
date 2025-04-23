# CREATE String строки
a = 'привет' # Одинарные кавычки
b = "привет" # Двойные кавычки
c = "я 'знаю' Python" # Компинированные кавычки
d = 'я "знаю" Python' # Можно и так
e = 'я "знаю' Python" # А так нельзя (кавычки вперемешку)

a = 123 # Целочисленный тип
a = str(a) # Результат, '123'
str([1, 1.1, 'a']) # Результат, "[1, 1.1, 'a']"
str(True) # Результат, 'True'
str(None) # Результат, 'None'

a = 'привет'
b = 'Иван'
с = f"{a} я {b}" # "привет я Иван"

# RETRIVE
a = 'привет'
print(a)
print('Иван')

a = 'привет'
a[0] # 'п'
a[1] # 'р'
a[2] # 'и'
a[3] # 'в'
a[4] # 'е'
a[5] # 'т'
a[6] # Ошибка, вышли за границы
a[-1] # 'т'
a[-2] # 'е'
a[-3] # 'в'
a[-4] # 'и'
a[-5] # 'р'
a[-6] # 'п'
a[-7] # Ошибка, вышли за границы

# UPDATE
a = 'привет'
a[0] = 'б' # Хотели получить 'бривет', а получили ошибку, что строку нельзя изменять TypeError: 'str' object does not support item assignment
a = 'бривет' # Для изменения придется полностью присвоить новое значение

# DELETE
a = 'привет'
del a[0] # Ошибка, элемент у строки нельзя удалить TypeError: 'str' object doesn't support item deletion
del a # Полное удаление переменной 'a'

# Действия со строками
a = 'привет'
b = 'Мир'
c = a + b
print(c) # 'приветМир'
c += b # 'приветМирМир'

a = 'привет'
b = 2
c = a * b
print(c) # 'приветпривет'
a *= b # "a" равно 'приветпривет'

a = '' # Две одинарные кавычки
b = "" # Две двойные кавычки
c = str

# Методы
help(str) # Информация о строках
a = 'привет мир'
a.count('р') # 2. Сколько раз 'р' встречается в 'привет мир'
a.find('вет') # 3. На каком индексе в 'привет мир' начинается первое входение слова 'вет'. Если такого слова нет то вернет -1
a.index('вет') # 3. На каком индексе в 'привет мир' начинается первое вхождение слова 'вет'. Если такого слова нет то вернет ошибку
a.rfind('р') # 9. На
a.rindex('р')

a = 'привет Мир'
a.removeprefix('пр')
a.removeprefix('ир')
a.replace('р', 'Р')
a.replace('р', 'Р', 1)
a.capitalize()
a.lower()
a.upper()
a.swapcase()

'привет'.isalpha()
'привет мир'.isalpha()
'123'.isdigit()
'123abc'.isalnum()
'привет'.isascii()
'\n\t\r'.isspace()
'123\n'.isprintable()
'Привет мир'.istitle()
'привет мир'.islower()
'ПРИВЕТ МИР'.isupper()

'int'.isidentifier()
'привет мир'.startswith('пр')
'привет мир'.endswith('мир')

' \t привет \n'.strip()
'ww привет ww'.strip('w')
'ww привет ww'.rstrip('w')
'ww привет ww'.lstrip('w')
'привет мир'.partition('и')
'привет мир'.rpartition('и')

'www \t привет \n www'.split()
'www_привет_www'.split('_')
'www_привет_www'.rsplit('_', 1)
a = ['www', 'привет', 'мир']
'-'.join(a)
'abc'.encode()

a = 'w\nпривет\tw мир'.split()
'_'.join(a)

a = input('Введи данные разделенные пробелом').split()

# Задача 1
length = 90
width  = 50

perimeter = length + width

# Задача 2
money = 10000
add = 5000

money += add

# Задача 3
hours = 5000
days = 0

days //= hours
hours %= hours

# Задача 4
volume = 1.44 * 1024 * 1024 # 1509949.44
pages = 100
lines = 50
characters = 25
necessary = 4

necessary *= characters

count = (necessary * lines * pages) // volume

# Задача 5
radius = 5
side = 5
pi = 3.1415

square = pi * (radius * radius)
length = 2 * pi * radius

perimeter = 4 * side
squareQ = side * side

print(f"Круг:{square} {length}. Квадрат: {perimeter} {squareQ}.")

# Задание 6
zero = '0'
one = '1'
two = '2'

str_numbers = zero * 20 + one * 50 + two * 30

print(str_numbers)
