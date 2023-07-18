def write_info(info): #создание функции для передачи данных в БАЗУ ДАННЫХ
    with open("data.txt","a",encoding="utf-8") as file:
        file.write(info)

def find_info(char):#создание функции по поиску данных в БАЗЕ ДАННЫХ
    with open("data.txt","r",encoding="utf-8") as file:
        lst_sel = []
        lst = file.readlines()
        count = 0
        for line in lst: # создание цикла для посика данных
            if char in line:
                count+=1
                print(f"{count}) {line.strip()}")
                lst_sel.append(line)
        return lst_sel

def view_all(): #создание функции для вывода данных в БАЗЕ ДАННЫХ
    with open("data.txt", "r", encoding="utf-8") as file: 
        print(file.read()) 

def change_data(old_data, new_data):#создание функции по изменению данных в БАЗЕ ДАННЫХ
    with open("data.txt","r",encoding="utf-8") as file:
        lst_old = file.readlines()
    with open("data.txt","w",encoding="utf-8") as file:
        for line in lst_old:
            if old_data in line:
                file.write(new_data)
            else:
                file.write(line)

def delete_data(old_data):#создание функции по удалению данных в БАЗЕ ДАННЫХ
    with open("data.txt","r",encoding="utf-8") as file:
        lst_old = file.readlines()
    with open("data.txt","w",encoding="utf-8") as file:
        for line in lst_old:
            if old_data in line:
                continue
            else:
                file.write(line)



