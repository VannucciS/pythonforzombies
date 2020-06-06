import string

arq = open('pg11.txt')
texto = arq.read()
texto = texto.lower()

for c in string.punctuation():
    texto = texto.replace( c, " ")
texto = texto.split()

dict = {}
for p in texto:
    if p not in dict:
        dict[p] = 1
    else:
        dict[p] += 1

arq.close()

print(dict['alice'])
                    

        
