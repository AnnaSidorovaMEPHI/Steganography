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