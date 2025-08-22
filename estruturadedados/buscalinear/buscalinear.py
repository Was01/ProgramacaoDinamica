def buscalinear(lista, elemento):
    for i in range(len(lista)):
        if lista[i]==elemento:
            return i
    return None


lista_estranha=[8,'5',32,0,'python',11]
elemento=0

indice=buscalinear(lista_estranha,elemento)

if indice is not None:
    print('O índice do elemento {} é {}.'.format(elemento,indice))
else:
    print('O elemento {} não se encontra na lista.'.format(elemento))