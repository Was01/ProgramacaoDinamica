def inverte_lista(lista):
    tamanho=len(lista)
    limite=tamanho//2
    for i in range (limite):
        lista[i],lista[tamanho-1-i]=lista[tamanho-1-i],lista[i]
    return lista
       
       
 # Teste
 
minha_lista=[10,20,30,40,50]
print(inverte_lista(minha_lista))