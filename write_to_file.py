# функция записывает данные в файл



def load_data_to_file(filename, text):
    try:
        with open('new_file.txt', 'x', encoding='utf-8') as file:
            file.write(text)
    except FileExistsError:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)

if __name__ == '__main__':
    text = input('Введите что-либо:')
    load_data_to_file('new_file.txt', text)




