from functions import bin_alpha,bin_secret,extract_secret    

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

    
    return extract_secret(binary_secret) #возвращает прямо строку уже декодированную
            
    



if __name__ == "__main__":
    #stego = spaces_in_the_end_encode('onegin.txt', 'abasd')
    #with open('steg.txt', 'w') as file:
    #    for i in stego:
    #        file.write(i)

    destego = spaces_in_the_end_decode('steg.txt')
    print(destego)