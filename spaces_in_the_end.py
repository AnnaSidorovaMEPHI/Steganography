def bin_alpha(alpha):
    bin_alpha = bin(ord(alpha))[2:]
    return  '0' * (8 - len(bin_alpha)) +  bin_alpha


def bin_secret(secret):
    bin_secret = ''
    for alpha in secret:
        bin_secret += bin_alpha(alpha)
    return bin_secret
    

def spaces_in_the_end_encode(file, secret):
    binary_secret = bin_secret(secret)
    result = list()
    with open(file, 'r') as file:
        for line_number, line in enumerate(file):
            if line_number < len(binary_secret):
                space = int(binary_secret[line_number]) * " "
                result.append(line.rstrip() + space + '\n')
            else:
                result.append(line.rstrip() + '\n')
    return result #на выходе массив из строк, в которых серктеное сообзение
                  #этот массив потом по красоте надо записать в файл


def spaces_in_the_end_decode(file):
    binary_secret = ''
    with open(file, 'r') as file:
        for line in file:
            if len(line) > 1:
                if line[-2] == ' ':
                    binary_secret += '1'
                else:
                    binary_secret += '0'
            else:
                binary_secret += '0'

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
    return secret #возвращает прямо строку уже декодированную
            
    



if __name__ == "__main__":
    #stego = spaces_in_the_end_encode('onegin.txt', 'abasd')
    #with open('steg.txt', 'w') as file:
    #    for i in stego:
    #        file.write(i)

    destego = spaces_in_the_end_decode('steg.txt')
    print(destego)