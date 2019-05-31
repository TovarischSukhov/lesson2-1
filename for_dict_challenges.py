# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]	
for name in students:
    print(name['first_name']+':',students.count(name))
    students.remove(name)
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
	

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
count = 0
name = ""
for i in students:
    if students.count(i) > count:
        count = students.count(i)
        name = i['first_name']
print("Самое частое имя среди учеников:", name)

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
class_1 = school_students[0]
class_2 = school_students[1]
count1 = 0
count2 = 0 
for i in class_1:
    if class_1.count(i) > count1:
        count1 = class_1.count(i)
        name1 = i['first_name']

for i in class_2:
    if class_2.count(i) > count2:
        count2 = class_2.count(i)
        name2 = i['first_name']


print("Самое частое имя в классе 1:",name1)
print("Самое частое имя в классе 2:",name2)

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for clas in school:
    m = 0
    for student in clas['students']:
        if is_male[student['first_name']] == True:
	          m += 1
    print("В классе",clas['class'],(len(clas['students'])-m),"девочки и",m,"мальчика")

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
mclass = ''
wclass = ''
for clas in school:
    m = 0
    w = 0
    for student in clas['students']:
        if is_male[student['first_name']] == True:
	          m += 1
    w = len(clas['students'])-m
    if m > w:
        mclass = clas['class']
    else:
        wclass = clas['class'] 
print("Больше всего мальчиков в классе:",mclass)
print("Больше всего девочек в классе:",wclass)
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a