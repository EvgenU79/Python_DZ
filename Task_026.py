# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def recur(numb,stepen):
    if stepen == 1:
        return numb
    return numb*recur(numb,stepen-1)
numb = int(input("Введите число: "))
stepen = int(input("Введите степень: "))
print(recur(numb,stepen))