# Entre 1067 e 3627 (inclusive), quantos números são pares e
# também divisíveis por 7?

lista = []
for x in range (1067, 3627):
    if x % 2 == 0 and x % 7 == 0:
        lista.append(x)
print (len(lista))
