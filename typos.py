from functions import bin_alpha, bin_secret, extract_secret
!pip install autocorrect
from autocorrect import spell
import random

def make_a_dict():
    list='m q w e r t y i u o p a s d f g h j k l z x c v b n m q' #собл.цикличность
    list=list.split()
    d={}
    for i in range(1,len(list)-1):
        d[list[i]]=list[i+1]
    return(d) 

def typos_encode(file1,file2):
    d=make_a_dict()
    with open(file1,'r') as file:
        message=bin_secret(file.read())
    with open(file2,'r') as file:  
        text=file.read()
    newtext=''
    k=0
    j=0
    while k<len(text):
        if text[k-1]==' ' and text[k]!=' ' and j<len(message) or k==0:
            if message[j]=='1':
                newtext+=text[k]+d[text[k].lower()]      
            else:
                newtext+=text[k] 
            j+=1
        else:
            newtext+=text[k]
        k+=1
    return newtext

def typos_decode(text):
    k=0
    message=''
    while k<len(text):
        if text[k-1]==' ' and text[k]!=' ' or k==0 and  text[k].isalpha():
            word=''
            j=k
            while text[j]!=' ' and j<len(text)-1:
                word+=text[j]
                j+=1
            if word.lower()==spell(word).lower():
                message+='0'
            else:
                message+='1'
        else:
            pass
        k+=1
    return extract_secret(message)

if __name__ == "__main__":
    text=typos_encode('./textfiles/secret.txt','./textfiles/graphology.txt')
    code=typos_decode(text)
    print(code)

