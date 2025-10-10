class Node:
  def __init__(self,data):
    self.data=data
    self.next=None


class Lista:
  def __init__ (self):
    self.head=None
    self.__size=0

  def append(self,data):
    novo_no=Node(data)
    if self.head is None:
      self.head=novo_no
    else:
      pointer=self.head
      while pointer.next is not None:
        pointer=pointer.next
      pointer.next=novo_no
    self.__size+=1

  def __len__(self):
    return self.__size

  def __getitem__(self, index):
    if index < 0 or index >= self.__size:
      raise IndexError('List index out of range')
    pointer = self.head
    for i in range(index):
      pointer = pointer.next
    return pointer.data


  def __setitem__(self,index,data):
    if index<0 or index>=self.__size:
      raise IndexError('List index out of range')
    pointer=self.head
    for i in range(index):
      pointer=pointer.next
    pointer.data=data

  def index(self, elemento):
    pointer=self.head
    i=0
    while pointer is not None:
      if pointer.data==elemento:
        return i
      else:
        pointer=pointer.next
        i+=1
    raise ValueError(f'{elemento} is not in list')

  def insert(self,index,data):
    if index==self.__size:
      return self.append(data)
    if index<0 or index>=self.__size:
      raise IndexError('List index out of range')
    novo_no=Node(data)
    if index==0:
      novo_no.next=self.head
      self.head=novo_no
    else:
      pointer=self.head
      for i in range(index-1):
        pointer=pointer.next
      novo_no.next=pointer.next
      pointer.next=novo_no
    self.__size+=1

  def remove(self,index):
    if index<0 or index>=self.__size:
      raise IndexError('List index out of range')
    if index==0:
      self.head=self.head.next
    else:
      pointer=self.head
      for i in range(index-1):
        pointer=pointer.next
      pointer.next=pointer.next.next
    self.__size-=1

