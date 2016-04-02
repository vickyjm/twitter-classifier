
import re

def removeEmoji(t) :
    text = t
    print(text) 

    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    print(emoji_pattern.sub(r'', text))

def removeSymbols(t) :
    string = t
    new_str = re.sub('[^a-zA-Z0-9\n\./:><=!?()-_+~`"\'|,éáíóúüÁÉÍÓÚÜñÑ€$¥£]', ' ', string)
    print(new_str)

def replaceText(f) :
    string = open("./UserDocs/"+f).read()
    new_str = re.sub('[^a-zA-Z0-9\n\._|,éáíóúüÁÉÍÓÚÜñÑ€$¥£]', ' ', string)
    # Reemplazando acentos por minusculas
    new_str = re.sub('á|Á','a',new_str)
    new_str = re.sub('é|É','e',new_str)
    new_str = re.sub('í|Í','i',new_str)
    new_str = re.sub('ó|Ó','o',new_str)
    new_str = re.sub('ú|ü|Ú|Ü','u',new_str)

    open("./CleanUserDocs/"+f, 'w').write(new_str)
1
# removeEmoji("")
# removeSymbols("")

for i in range(1,2001) :
    filename=str(i)+".txt"
    replaceText(filename)

# prueba = "holaÁaá vale como estas Ósea"

# newprueba = re.sub('á|Á','a',prueba)
# newnewprueba = re.sub('Ó','o',newprueba)
# print(newnewprueba)




