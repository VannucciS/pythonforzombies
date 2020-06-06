arquivo = open('números.txt', 'w')
for linha in range(1,101,2):
    arquivo.write('linha %d\n' %linha)
arquivo.close()
