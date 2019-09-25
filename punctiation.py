from functions import *
from random import randint


def punct_encode(file, secret):
    possible_punct = ('!', ';')
    secret = bin_secret(secret)
    with open(file, 'r') as file:
        data = file.read().replace(';', '.').replace('!', '.')
    
    waste = [i for i in data]
    step = 0
    i = 0
    while i < len(secret):
        if waste[i + step] == '.': 
            if secret[i] == '1':
                waste[i + step] = possible_punct[randint(0,1)] 
            i += 1
        else:
            step += 1
    return ''.join(waste) #на выходе строка, которую нужно записать в файл


def punct_decode(file):
    secret = ''
    with open(file, 'r') as file:
        data = file.read()
    for i in data:
        if i == '!' or i == ';':
            secret += '1'
        elif i == '.':
            secret += '0'
    print(secret)
    return extract_secret(secret) #на выходе готовый секрет

'''
if __name__ == "__main__":
    with open('steg.txt', 'w') as file:
        file.write(punct_encode('textfiles/onegin.txt', 'Top Secret 1001101'))

    print(punct_decode('steg.txt'))
'''
    