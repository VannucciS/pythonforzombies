def embaralha (texto):
    import random
    lista = list(texto)
    random.shuffle(lista)
    " ".join(lista)
    return print("".join(lista))
    

embaralha("123456")



