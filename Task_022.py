# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n1 = int(input("Введите количество элементов списка 1: "))
n2 = int(input("Введите количество элементов списка 2: "))
lst_1 = [int(input()) for i in range(n1)]
lst_2 = [int(input()) for i in range(n2)]

i = set(lst_1).intersection(set(lst_2))
print(i)