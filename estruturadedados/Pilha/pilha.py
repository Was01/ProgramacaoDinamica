class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class Stack():
  def __init__(self):
    self.topo=None
    self.__size=0

  def push(self,data):
    novo_no=Node(data)
    novo_no.next=self.topo
    self.topo=novo_no
    self.__size+=1

  def peek(self):
    if self.topo is None:
      return None
    return self.topo.data
