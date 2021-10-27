# функция для шифрования
def encrypt(text):

    encrypted = ''
    global lang
    n = int(input('На сколько символов оформим сдвиг?\n'))

    for ch in text:
        if lang == 2:  # кириллица

            if 1040 <= ord(ch) <= 1071:  # строчные буквы
                if ord(ch) + n > 1071:
                    encrypted += chr(1039 + (ord(ch) + n - 1071))
                else:
                    encrypted += chr(ord(ch) + n)

            elif 1072 <= ord(ch) <= 1103:   # прописные
                if ord(ch) + n > 1103:
                    encrypted += chr(1071 + (ord(ch) + n - 1103))
                else:
                    encrypted += chr(ord(ch) + n)

            else:
                encrypted += ch

        else:   # латиница
            if 65 <= ord(ch) <= 90:  # строчные
                if ord(ch) + n > 90:
                    encrypted += chr(64 + (ord(ch) + n - 90))
                else:
                    encrypted += chr(ord(ch) + n)

            elif 97 <= ord(ch) <= 122:  # прописные
                if ord(ch) + n > 122:
                    encrypted += chr(96 + (ord(ch) + n - 122))
                else:
                    encrypted += chr(ord(ch) + n)

            else:
                encrypted += ch

    return encrypted


# функция дешифрования
def decrypt(text):

    decrypted = ''
    global lang
    print('Выбирайте подходящий вариант:')

    if lang == 1:
        lng = 26
    else:
        lng = 32
    
    for n in range(1, lng):
        for ch in text:

            if lang == 2:   # кириллица
                if 1040 <= ord(ch) <= 1071:  # строчные
                    if ord(ch) - n < 1040:
                        decrypted += chr(1072 - (n - (ord(ch) - 1040)))
                    else:
                        decrypted += chr(ord(ch) - n)

                elif 1072 <= ord(ch) <= 1103:  # прописные
                    if ord(ch) - n < 1072:
                        decrypted += chr(1104 - (n - (ord(ch) - 1072)))
                    else:
                        decrypted += chr(ord(ch) - n)

                else:
                    decrypted += ch

            else:  # латиница
                if 65 <= ord(ch) <= 90:  # строчные
                    if ord(ch) - n < 65:
                        decrypted += chr(91 - (n - (ord(ch) - 65)))
                    else:
                        decrypted += chr(ord(ch) - n)

                elif 97 <= ord(ch) <= 122:  # прописные
                    if ord(ch) - n < 97:
                        decrypted += chr(123 - (n - (ord(ch) - 97)))
                    else:
                        decrypted += chr(ord(ch) - n)

                else:
                    decrypted += ch

        print(f'{decrypted} - один из вариантов')
        decrypted = ''


def start():
    while True:
        way = int(input('Шифруем(1) или дешифруем(2)?\n'))
        if way not in [1, 2]:
            print('Введите корректное значение')
        else:
            break

    while True:
        lang = int(input('Английский(1) или русский(2)?\n'))
        if lang not in [1, 2]:
            print('Введите корректное значение')
        else:
            break

    text = input('Введите текст на выбранном языке\n')
    if way == 1:
        print(encrypt(text))
    else:
        decrypt(text)
        
        
 start()
