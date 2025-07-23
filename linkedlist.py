class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
    def iab(self,data):
        newnode=Node(data)            
        newnode.next=self.head
        self.head=newnode
        print(f"{data} inserted from begin.")
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
        l1.iab(data)
    elif choice=='2':
        l1.display()
    elif choice=='3':
        print("exit the operation")        