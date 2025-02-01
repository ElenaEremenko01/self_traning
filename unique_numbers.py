# Функция принимает список чисел.
# Возвращает уникальные числа в порядке возрастания


def unique_number(number_list):
    unique_set = set(number_list)
    return list(unique_set)


if __name__ == "__main__":
    print(unique_number([1, 12, 3, 4, 6, 8, 8, 9, 9]))
