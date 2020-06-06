lista = []
import random
while len(lista) < 16:
    num = random.randint(1,17)
    if num not in  lista:
        lista.append(num)

    
print(sorted(lista))
