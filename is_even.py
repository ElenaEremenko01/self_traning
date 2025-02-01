# написать функцию is_even


def is_even(number):
    try:
        if number % 2 == 0:
            return True
        else:
            return False
    except TypeError:
        print("Вы можете ввести только число")


if __name__ == "__main__":
    print(is_even("vif"))
