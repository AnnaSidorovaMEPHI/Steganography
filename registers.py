def bin_alpha(alpha):
    bin_alpha = bin(ord(alpha))[2:]
    return  '0' * (8 - len(bin_alpha)) +  bin_alpha


def bin_secret(secret):
    bin_secret = ''
    for alpha in secret:
        bin_secret += bin_alpha(alpha)
    return bin_secret


def extract_secret(binary_secret):
    parsed = []
    part = ''
    step = 0
    for i in binary_secret:
        part += i
        step += 1
        if step == 8:
            if part != '00000000':
                parsed.append(part)
                part = ''
                step = 0

    secret = ''
    for part in parsed:
        secret += chr(int(part, 2))
    return secret


def registers_encode(file, secret):
    secret = bin_secret(secret)
    with open(file, 'r') as file:
        data = file.read()
    data = data.lower()
    waste = [i for i in data]

    step = 0
    i = 0
    while i < len(secret):
        if waste[i + step].isalpha():
            if secret[i] == '1':
                waste[i + step] = waste[i + step].upper()
            i += 1
        else:
            step += 1
    return ''.join(waste) #на выходе текст, который нужно поместить в файл
    


def registers_decode(file):
    secret = ''
    with open(file, 'r') as file:
        data = file.read()
    for i in data:
        if i.isalpha():
            if i.isupper():
                secret += '1'
            else:
                secret += '0'
    return extract_secret(secret) #на выходе готовая строка


if __name__ == "__main__":
    a = registers_encode('./textfiles/onegin.txt', 'Anna Sidorova')
    with open('steg.txt', 'w') as file:
        file.write(a)

    print(registers_decode('./textfiles/steg.txt'))
