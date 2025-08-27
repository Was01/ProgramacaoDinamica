class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


no1=Node(5)
print(no1.data)


no2=Node(-3)
print(no2.data)


no1.next=no2
print(no1.next.data)