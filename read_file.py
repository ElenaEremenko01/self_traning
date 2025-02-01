# Функция читает данные с файла и вводит в консоль

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        print(data)

if __name__ == '__main__':
    read_file('new_file.txt')

