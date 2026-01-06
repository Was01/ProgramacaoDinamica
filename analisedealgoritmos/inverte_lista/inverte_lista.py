def inverte_lista(lista):
    tamanho=len(lista)
    limite=tamanho//2
    for i in range(limite):
        aux=lista[i]
        lista[i]=lista[tamanho-1-i]
        lista[tamanho-1-i]=aux
    return lista



def inverte_lista2(lista):
    nova_lista=[]
    tamanho=len(lista)
    for i in range(tamanho):
        nova_lista.append(lista[tamanho-1-i])
    return nova_lista

lista=[1,2,3,4,5]

lista2=inverte_lista(lista)


print(lista2)
print(inverte_lista(lista2))



