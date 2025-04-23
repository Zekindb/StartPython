# # CREATE
# a = [1, 1.1, 'a', [1], (1, 1.1), {1, 2}, {'a': 1}, None, True]
#
# a = []
# b = list()
#
# a = (1, 2.1, 3)
# list(a)
# b = list('abc')
#
# RETRIVE
# a = [1, 1.1, 'a']
# print(a)
# print([1, 1.1, 'a'])
#
# a = [1, 1.1, 'a']
# a[0]
# a[1]
# a[2]
# a[3]
# a[-1]
# a[-2]
# a[-3]
# a[-4]
#
# a = [1, 2, 3]
# a.index(3)
#
# # UPDATE
# a = [1, 1.1, 'a']
# a[0] = 'a'
# a[1] = 'б'
# a[-1] = 'в'
# a = [1, 2, 3]
#
# a = [1, 2, 3]
# a.append(4)
#
# a.append(['a', 'b'])
#
# a = [1, 2, 3]
# a.insert(0, 4)
#
# a = [1, 2, 3]
# a.insert(3, 4)
#
# a = [1, 2, 3]
# a.insert(-1, 4)
#
# a = [1, 2, 3]
# a.extend([4, 5, 6])
#
# # DELETE
# a = [1, 1.1, 'a']
# del a[0]
# del a[-1]
# del a[-1]
# del a
#
# a = [1, 2, 3]
# a.clear()
#
# a = [1, 2, 3]
# a.pop()
#
# a = [1, 'ab', 3]
# a.pop(1)
#
# a = [1, 2, 'ab']
# a.remove('ab')

# Задание
group120 = [
    'Агафонов',
    'Арасланов',
    'Дудин',
    'Дюндин',
    'Жариков',
    'Звягинцев',
    'Кирилова',
    'Колосков',
    'Кураев',
    'Кутовой',
    'Лесовой',
    'Мерзляков',
    'Невзоров'
]

half1 = group120[:6]
print(half1)
half2 = group120[6:]
print(half2)

a = 1, 2, 3
b = str(a)
print(b)
print(type(b))

a = 1, 5.5, "hello"
b = list(a)
print(b)
print(type(b))

a = int(input("Введите целое число: - "))

if a % 2 == 0:
    print(f'Число {a} является четным')
else:
    print(f'Число {a} является нечетным')

# Задача на подсчет символов
a = str(input("Введите любую строку: - "))
print(len(a))
