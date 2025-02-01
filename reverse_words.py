# функция переворачивает слова, но не меняет их порядок

def reverse_words(sentence):
    words = sentence.split()
    reversed_list = []
    for word in words:
        reversed_list.append(word[::-1])
    print(' '.join(reversed_list))


if __name__ == '__main__':
    reverse_words('hello world')
