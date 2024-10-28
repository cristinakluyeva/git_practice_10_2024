import os

def clear_names(file_names: str)-> list:
    """Функция для очистки имен от лишних символов"""
    new_names_list = list()
    file_names_adress = os.path.abspath(file_names)
    with open(file_names_adress + , "r") as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name=""
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_names_list.append(new_name)
    return new_names_list


if __name__== "__main__":
    cleared_names = clear_names("names.txt")

    for i in cleared_names:
        print(i)