from functions import *


def change_alphabet_encode(file, secret):
    secret = bin_secret(secret)
    with open(file, 'r') as file:
        data = file.read()
    data = data.replace('е', 'e')

    waste = [i for i in data]
    step = 0
    i = 0
    while i < len(secret):
        if waste[i + step] == 'e': #english
            if secret[i] == '1':
                waste[i + step] = 'е' #russian
            i += 1
        else:
            step += 1
    return ''.join(waste) # тут на выходе имеем строку, которую просто в файл записать


def change_alphabet_decode(file):
    secret = ''
    with open(file, 'r') as file:
        data = file.read()
    for i in data:
        if i == 'е':
            secret += '1'
        elif i == 'e':
            secret += '0'
    return extract_secret(secret) #тут на выходе имеем декодированную строку



if __name__ == "__main__":
    with open('steg.txt', 'w') as file:
        file.write(change_alphabet_encode('onegin.txt', 'Top Secret'))

    print(change_alphabet_decode('steg.txt'))