import string
import random


def pwd_len():
    """ Taking password length from user """
    while True:
        password_length = input('How much length for password u want ? Minimum length is 6 and Maximum length is 25 : ')
        try:
            password_length = int(password_length)
            if 6 <= password_length <= 25:
                break
            else:
                print('{} is not in range'.format(password_length))
        except ValueError:
            print('{} is not an integer'.format(password_length))
    return password_length


def alpha_len(password_length):
    """ How much alphabets user wants """
    while True:
        alphabet_length = input('How much alphabets you want in password? At least 1 : ')
        try:
            alphabet_length = int(alphabet_length)
            if 1 <= alphabet_length <= (password_length - 2):
                break
            else:
                print('{} is not in range'.format(alphabet_length))
        except ValueError:
            print('{} is not an integer'.format(alphabet_length))
    return alphabet_length


def number_len(password_length):
    """ How much numbers user wants """
    while True:
        numb_length = input('How much numbers you want in password? At least 1 : ')
        try:
            numb_length = int(numb_length)
            if 1 <= numb_length <= (password_length - 2):
                break
            else:
                print('{} is not in range'.format(numb_length))
        except ValueError:
            print('{} is not an integer'.format(numb_length))
    return numb_length


def symbol_len(password_length):
    """ How much symbols user wants """
    while True:
        symb_length = input('How much symbols you want in password? At least 1 : ')
        try:
            symb_length = int(symb_length)
            if 1 <= symb_length <= (password_length - 2):
                break
            else:
                print('{} is not in range'.format(symb_length))
        except ValueError:
            print('{} is not an integer'.format(symb_length))
    return symb_length


def check_len(password_length, alphabet_length, numb_length, symb_length):
    """ Check user enters the right Values for each category or not """
    return (symb_length + alphabet_length + numb_length) == password_length


if __name__ == '__main__':
    symbols = '!@#$%^&*()_+-=[]{}|:;",./<>?'
    """ Taking input lengths from user """
    while True:
        pwd_length = pwd_len()
        alpha_length = alpha_len(pwd_length)
        number_length = number_len(pwd_length)
        symbol_length = symbol_len(pwd_length)
        if check_len(pwd_length, alpha_length, number_length, symbol_length):
            break
        else:
            continue

    password = []   # dummy list to store the password
    """ update the password list with alphabets """
    while alpha_length:
        password.append(string.ascii_letters[random.randint(0, len(string.ascii_letters))])
        alpha_length -= 1

    """ update the password list with numbers """
    while number_length:
        password.append(random.randint(0, 9))
        number_length -= 1

    """ update the password list with symbols """
    while symbol_length:
        password.append(symbols[random.randint(0, len(symbols))])
        symbol_length -= 1

    """ shuffle the password """
    random.shuffle(password)
    password = ''.join(str(ele) for ele in password)

    print('your generated password for given lengths is {}'.format(password))
