class Node:
    def __init__(self,data):
        self.data =data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
        self._size=0

    def append(self,elemento):
        if self.head:
            pointer=self.head
            while(pointer.next):
                pointer=pointer.next
            pointer.next=Node(elemento)
        else:
            self.head=Node(elemento)
        self._size+=1
    
    def __len__(self):
        return self._size
    
    def __getitem__(self,index):
        pointer=self.head
        for i in range(index):
            if pointer:
                pointer=pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            return pointer.data
        raise IndexError("List index out of range")
    
    def __setitem__(self,index,elemento):
        pointer=self.head
        for i in range(index):
            if pointer:
                pointer=pointer.next
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


lista=LinkedList()
lista.append('Suelen')
lista.append('Samara')
lista.append("Marli")




print(lista[0])
print(lista[1])





print(lista.index('Marli'))