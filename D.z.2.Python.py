"""Задача 1. Напишите программу, которая принимает на вход вещественное или целое число
 и показывает сумму его цифр."""


def InputNum(text):
    right = False
    while not right:
        try:
            number = float(input(f"{text}"))
            right = True
        except ValueError:
            print("Не верный ввод!")
    return number


def sumNum(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


num = InputNum("Введите число: ")

print(f"Сумма цифр = {sumNum(num)}")





# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def InputNum(text):
    right = False
    while not right:
        try:
            number = int(input(f"{text}"))
            right = True
        except ValueError:
            print("Не верный ввод! ")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = InputNum("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")






'''Задача 3. Реализуйте алгоритм перемешивания списка.
Список размерностью 10 задается случайными целыми числами, выводится на экран, затем перемешивается,
опять выводится на экран. SHUFFLE нельзя юзать!'''




import random


def get_list(n, left, right):
    return [random.randint(left, right) for i in range(n)]


def sample_list(lst):
    return random.sample(lst)


n = 10
left = -20
right = 30

mylist = get_list(n, left, right)
print(mylist)
mylist = random.sample(mylist, len(mylist))
print(str(mylist))

