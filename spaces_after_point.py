from functions import bin_alpha,bin_secret,extract_secret

def spaces_after_point_encode(file1,file2):
    with open(file1,'r') as file:
        message=bin_secret(file.read())
    with open(file2,'r') as file:  
        text=file.read()
    k=0
    j=0
    newtext=''
    while k<len(text):
        newtext+=text[k]
        if text[k]=='.':
            if j<len(message):
                if text[k+1]==' ':
                    newtext+=' '*int(message[j])
                else:
                    newtext+=' '*(int(message[j])+1)
            j+=1
        k+=1
    #with open('./result.txt','w') as file:  
        #file.write(newtext)
    return newtext #может, файл, а может, и нет..

def spaces_after_point_decode(text):
    k=0
    message=''
    while k<len(text):
        if text[k]=='.':
            if text[k+2]==' ':
                if text[k+3]==' ': # избежание случаев, когда много пробелов изначально
                    pass
                else:
                    message+='1'
            else:
                message+='0'
        k+=1        
    return extract_secret(message)

if __name__ == "__main__":
    #text=spaces_after_point_encode('./textfiles/secret.txt','./textfiles/acupoftea.txt')
    text=spaces_after_point_encode('./textfiles/secret.txt','./textfiles/Onegin.txt')
    print(spaces_after_point_decode(text))
        