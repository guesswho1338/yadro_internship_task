import sys

if len(sys.argv) == 3:
    namefile = sys.argv[1]
    find_string = sys.argv[2]
else:
    print("Неправильное количество аргументов:\nИспользование: python3 script.py [имя файла] [строка для поиска]")
    sys.exit(1)


with open(namefile) as file:
    for string in file:
        if find_string in string:
            print(string.strip())
