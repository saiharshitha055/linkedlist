class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            print(f"{data} inserted at end/ will be first node")
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode
        print(f"{data} inserted last")    
    def display(self):
        current=self.head
        if not current:
            print("LL-Empty")    
            return
        while current:
            print(current.data,end='---')
            current=current.next
        print("None")
l1=Linkedlist()            
while True:
    print("\n linkedlist-insert at begin")
    print("1.insert")
    print("2.display")
    print("3.exit")
    choice=input("enter ur choice")
    if choice=='1':
        data=int(input("enter a value to insert"))
        l1.iae(data)
    elif choice=='2':
        l1.display()
    elif choice=='3':
        print("exit the operation")        