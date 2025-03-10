#!/usr/bin/env python3
# by Allori  https://github.com/Allorion/
import turtle  # Импортируем графический модуль
from itertools import combinations  # Импортируем модуль для выборки
import random  # Импортируем модуль случайного выбора из списка

# Создаем черепашку и задаем ей скорость
pen = turtle.Turtle()  # Создаем черепашку
pen.speed(1)  # Задаем скорость передвижения пера

# Создаем словарь c координатами вершин шестиугольника
a = {
    '1': (100.00, 0.00),
    '2': (150.00, 86.60),
    '3': (100.00, 173.21),
    '4': (0.00, 173.21),
    '5': (-50.00, 86.60),
    '6': (-0.00, 0.00),
}

# Создаем список цветов для линий
color = ['#FF69B4', '#8B0000', '#00FFFF', '#00008B', '#FFFF00', '#D2691E', '#FFA07A', '#ADFF2F', '#008B8B', '#800080',
         '#F0E68C', '#696969', '#D2691E', '#7FFFD4', '#228B22', '#FF00FF', '#000000', '#C71585', '#e9967a', '#F0E68C']

# Создаем функцию в которой черепашка будет рисовать правильный шестиугольник
for j in range(1):
    pen.speed(1)  # Задаем скорость движения пера
    n = 6
    dlina = 20
    sum_angle = (6 - 2) * 180
    if sum_angle % n == 0:
        angle = sum_angle // n

        for i in range(6):
            pen.forward(100)
            pen.left(180 - angle)
            # p = pen.pos()               #Код для нахождения координатов вершин шестиугольников
            # print(p)

    # Создаем функцию, которая будет подбирать уникальные сочетания вершин треугольника
    for i in combinations('123456', 3):
        l = list(color)
        random.shuffle(l)  # Перемешиваем список
        for y in l:
            pen.color(y)  # Красим перо в выбранный цвет
        r = ''.join(i)  # Создаем список вершин треугольника
        print(i)


        # Создаем функцию в которой исключим черчение линии при переходе от первых вершин (1 к 2 и 2 к 3)
        def lines():
            pen.up()
            pen.goto(a[r[0:1]])
            pen.down()
            pen.goto(a[r[1:2]])
            pen.goto(a[r[2:3]])
            pen.goto(a[r[0:1]])


        # Напишем проверку для перескока вершин
        count = 1
        if r[0:1] != 0:
            count += 1
            lines()
        elif count != 3:
            lines()
        else:
            pen.goto(a[r[0:1]])
            pen.goto(a[r[1:2]])
            pen.goto(a[r[2:3]])
            pen.goto(a[r[0:1]])
# Сделаем закрытие окна черепашки по клику мыши
turtle.exitonclick()
