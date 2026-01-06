def tem_duplicados(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if (lista[i]==lista[j]):
                return True
    return False



lista='Café'
print(lista)

print(tem_duplicados(lista))