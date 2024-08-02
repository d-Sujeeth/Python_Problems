class node:
    def __init__(self,data):
        self.data=data
        self.pointer=None

class linkedlist:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            cur=self.head
            while cur.pointer is not None:
                cur=cur.pointer
            cur.pointer=newNode
    
l1=linkedlist()
l1.insert(6)
l1.insert(74)
print(l1)