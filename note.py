import os, fnmatch
from datetime import date, datetime


def note_list(str_date_begin = "", str_date_end = ""):
    if (len(str_date_begin) > 0) & (len(str_date_end) > 0):
        date_begin_obj = datetime.strptime(str_date_begin, "%d.%m.%y")
        date_end_obj = datetime.strptime(str_date_end, "%d.%m.%y")
        print("Период: " + date_begin_obj.date().strftime("%d.%m.%y") + "-" + date_end_obj.date().strftime("%d.%m.%y"))
    listOfFiles = os.listdir('.')
    pattern = "*.csv"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            change_date = os.path.getmtime(entry)
            ch_date_to_print = date.fromtimestamp(change_date)
            ch_date_to_check = datetime.strptime(ch_date_to_print.strftime("%d.%m.%y"), "%d.%m.%y")
            if (len(str_date_begin) > 0) & (len(str_date_end) > 0):
                if (ch_date_to_check.date() >= date_begin_obj.date()) & (ch_date_to_check.date() <= date_end_obj.date()):
                  print(entry + " " + ch_date_to_print.strftime("%d.%m.%y"))
            else:
                print(entry + " " + ch_date_to_print.strftime("%d.%m.%y"))


def write_note(file):
    print("Введите текст заметки (Для окончания введите пустую строку):")
    str1 = input()
    total_string = ""
    while (str1 != ""):
        total_string = (total_string + str1 + ";")
        str1 = input()
    file.write(total_string)

def choose_file(mode):
    if mode == "read":
        print("Введите имя файла для чтения(без указания расширения):")
        str_file = input()
        str_file = str_file + ".csv"
        file = open(str_file, "r")
    else:
        print("Введите имя файла для изменения(без указания расширения):")
        str_file = input()
        str_file = str_file + ".csv"
        file = open(str_file, "w")
    return file

def read_note(file):
    list_of_strings = []
    string_to_list = ""
    str1 = file.readline()
    if len(str1) == 0:
        list_of_strings.append("")
    else:
        for each in str1:
            if (each != ';'):
                string_to_list = string_to_list + each
            else:
                list_of_strings.append(string_to_list)
                string_to_list = ""
    return list_of_strings


def print_note(list_of_strings=[]):
    count = 0
    for str_of_list in list_of_strings:
        print(str(count) + ": " + str_of_list)
        count = count + 1


def edit_note():
    print("Введите имя файла для изменения(без указания расширения):")
    str_file = input()
    str_file = str_file + ".csv"
    file = open(str_file, "r")
    list_of_strings = read_note(file)

    print_note(list_of_strings)
    print("Введите номер строки для изменения: ")
    str_num = input()
    int_num = int(str_num)
    print("Текущее значение строки:")
    print(list_of_strings.pop(int_num))
    print("Введите новое значение:")
    list_of_strings.insert(int_num, input())
    print_note(list_of_strings)
    total_string = ""
    for str1 in list_of_strings:
       total_string = total_string + str1 + ";"
    file = open(str_file, "w")
    file.write(total_string)
    file.close()

def view_note():
    file = choose_file("read")
    list_of_strings = read_note(file)
    print_note(list_of_strings)
    file.close()

def add_new_note():
    print("Введите наименование файла: ")
    file_name = input()
    file_name = file_name + ".csv"
    file = open(file_name, "x")
    write_note(file)
    file.close()


def remove_note():
    print("Какой файл вы хотите удалить?(без указания расширения)")
    file_name = input()
    file_name = file_name + ".csv"
    os.remove(file_name)

note_list()
print("""Выберите действие:
      1 - Добавить новую заметку,
      2 - Вывести выбранную заметку
      3 - Редактировать выбранную заметку
      4 - Удалить заметку
      5 - Выбрать период вывода заметок""")
choise = input()
match choise:
    case "1":
        add_new_note()
    case "2":
        view_note()
    case "3":
        edit_note()
    case "4":
        remove_note()
    case "5":
        print("Введите дату начала периода:")
        str_date_begin = input()
        print("Введите дату окончания периода:")
        str_date_end = input()
        note_list(str_date_begin, str_date_end)
    case _:
        print("Нет такого варианта!")


