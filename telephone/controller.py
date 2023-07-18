# ДЗ
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

from database import * # Для вызова функций из файла database
from view import * # Для вызова функций из файла view

def main():
    while True: # для создание безконечного цикла запроса пользователя
        num = input_num() # создание переменной для опроса
        if num == 1:
            info = input_info() # создание переменной с данными ФИО,ДР, Телеф
            write_info(info)
            print("Пользователь добавлен")
        elif num ==2:
            char = input_char()
            find_info(char)# вызов функции по поиску
            print("Пользователь найден")
        elif num ==3:
            char = input_char()
            lst_sel = find_info(char)
            sel_num = select_num()
            info = input_info()
            change_data(lst_sel[sel_num-1],info)
            print("Изменения внесены")
        elif num ==4:
            char = input_char()
            lst_sel = find_info(char)
            sel_num = select_num()
            delete_data(lst_sel[sel_num-1])
            print("Данные удалены")
        elif num ==5:
            view_all()
        elif num ==6:
            print("Выход из программы...")
            break

main()



