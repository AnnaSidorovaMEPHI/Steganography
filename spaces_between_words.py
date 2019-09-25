from functions import bin_alpha,bin_secret,extract_secret

def preprocessing(text):
    text=text.replace('  ',' ')
    return text

def spaces_between_words_encode(file1,file2):
    with open(file1,'r') as file:
        message=bin_secret(file.read())
    with open(file2,'r') as file:  
        text=preprocessing(file.read())
    k=0
    j=0
    newtext=''
    while k<len(text):
        newtext+=text[k]
        if text[k-1]!=' ' and text[k]==' ' and text[k+1]!=' ':
            if j<len(message):
                newtext+=' '*int(message[j])
                j+=1
            k+=1
        else:
            k+=1
    return newtext 

def spaces_between_words_decode(text):
    k=0
    message=''
    while k<len(text):
        if text[k-1]!=' ' and text[k]==' ':
            if text[k]==' ' and text[k+1]!=' ':
                message+='0'
            elif text[k]==' ' and text[k+1]==' ' and text[k+2]!=' ':
                message+='1'
            else:
                pass
        k+=1  
    return extract_secret(message)

if __name__ == "__main__":
    text=spaces_between_words_encode('./textfiles/secret.txt','./textfiles/Onegin.txt')
    print(spaces_between_words_decode(text))