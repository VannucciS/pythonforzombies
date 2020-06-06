# Questão D. Daniela é uma pessoa muito supersticiosa. Para ela,
# um número é sortudo se ele contém o dígito 2 mas não o dígito 7.
# Então, na opinião dela, quantos números sortudos existem entre 18644 e 33087,
# incluindo os extremos?

lista =[]
for k in range (18644, 33088):
    n = list(str(k))
    
    if "2" in n and "7" not in n:
        lista.append(k)
print(len(lista))
