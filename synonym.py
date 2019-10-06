from functions import bin_alpha, bin_secret, extract_secret
import random

synonym={  #по версии онлайн-переводчика
    'studying' : 'education',
    'learning' : 'education',
    'teaching' : 'education',
    'training' : 'education',
    'doctrine' : 'education',
    'study' : 'educate',
    'learn' : 'educate',
    'train' : 'educate',
    'person': 'man' ,
    'man' : 'male', 
    'human' : 'male', 
    'husband' : 'male', 
    'guy' : 'male',
    'class' : 'lesson',
    'experience' :"lesson",
    'success' : 'luck', 
    'progress' : 'luck',
    'what' : 'which', 
    'who' : 'which',
    'pupils' : 'classmans', 
    'students' : 'learners',
    'schoolchilds' : 'students',
    'value' : 'meaning', 
    'role' : "meaning", 
    'importance' : 'meaning', 
    'existence' : 'living',
    'life' : 'living',
    'great' : 'grand',
    'world' : 'earth',
    'teacher' : 'tutor',
    'during' : 'in the process',
    'the' : 'a',
    'is' : 'be',
    'knowledge' : 'understanding',
    'experience' :'adventure',
    'of' : 'from',
    'grows' : 'develops',
    'passes' : 'goes',
    'significance' : 'relevancy',
    'to' : 'for',
    'in' : 'inside',
    'this' : 'that',
    'also' : 'too',
    'are' : 'is',
    'and': 'both',
    'become' : 'make',
    'emplloyees':'chief',
    'educated':'skilled' 
}


def synonym_encode(file1,file2):
    with open(file1,'r') as file:
        message = bin_secret(file.read())
    with open(file2,'r') as file:  
        text = file.read()
    newtext = ''
    symbols = 0
    symbolsofmes=0
    while symbols<len(text):
        word = ''
        if text[symbols-1]==' ' and text[symbols]!=' ' and symbolsofmes<len(message) or symbols==0:
            while text[symbols].isalpha():
                word += text[symbols]
                symbols += 1
            if message[symbolsofmes]=='1':
                newtext += synonym[word.lower()]+text[symbols]
            else:
                newtext+=word+text[symbols]
            symbolsofmes += 1
        else:
            newtext += text[symbols]
        symbols += 1
    return newtext


def synonym_decode(newtext):
    symbols = 0
    message = ''
    while symbols<len(text):
        word = ''
        if text[symbols-1]==' ' and text[symbols]!=' ' or symbols==0:
            while text[symbols].isalpha():
                word += text[symbols]
                symbols += 1
            if word.lower() in synonym.values():
                message += '1'
            else:
                message += '0'
        else:
            pass
        symbols += 1
    return extract_secret(message)


if __name__ == "__main__":
    text = synonym_encode('./textfiles/secret1.txt','./textfiles/textaboutlearning.txt')
    code = synonym_decode(text)
    print(code)
