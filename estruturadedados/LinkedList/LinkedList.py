class Node:
    def __init__(self,data):
        self.data =data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self._size=0

    def append(self, elemento):
        novo_no=Node(elemento)
        if self.head is None:
            self.head=novo_no
        else:
            pointer=self.head
            while pointer.next:
                pointer=pointer.next
            pointer.next=novo_no
        self._size+=1
    
    def __len__(self):
        return self._size
        
    
    def __getitem__(self,index):
        pointer=self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            return pointer.data
        raise IndexError("List index out of range")
    
    def __setitem__(self,index,elemento):
        pointer=self.head
        for i in range(index):
            if pointer:
                pointer =pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            pointer.data=elemento
        else:
            raise IndexError("List index out of range")
    
    def index(self,elemento):
        pointer=self.head
        i=0
        while pointer:
            if pointer.data==elemento:
                return i
            else:
                pointer=pointer.next
                i+=1
        raise ValueError("{} não está na lista".format(elemento))
    
    def insert(self,index,elemento):
        if index==0:
            novo_no=Node(elemento)
            novo_no.next=self.head
            self.head=novo_no
        else:
            pointer=self.head
            for i in range(index-1):
                if pointer:
                    pointer=pointer.next
                else:
                    raise IndexError("List index out of range")
            novo_no=Node(elemento)
            novo_no.next=pointer.next
            pointer.next=novo_no
        self._size+=1
    
    def remove(self, elemento):
        """ Remove a primeira ocorrência de um elemento da lista ligada."""
        # Caso 1: A lista está vazia.
        if self.head is None:
            raise ValueError(f'{elemento} não está na lista.')
        # Caso 2: O elemento a ser removido é o 'head' da lista.
        if self.head.data == elemento:
            self.head = self.head.next
            self._size -= 1
            return True
        # Caso 3: O elemento está em outro lugar na lista.
        ancestor = self.head
        pointer = self.head.next
        while pointer:
            if pointer.data == elemento:
                ancestor.next = pointer.next
                pointer.next = None  # Boa prática para desreferenciar o nó.
                self._size -= 1
                return True  # 'return' colocado corretamente após a remoção.
            ancestor = pointer
            pointer = pointer.next

         # Caso 4: O elemento não foi encontrado na lista.
        raise ValueError(f'{elemento} não está na lista.')

lista=LinkedList()

lista.append('Washington')
lista.append('Marli')
lista.remove('Marli')
lista.remove('Washington')

for i in range(len(lista)):
    print (lista[i])

