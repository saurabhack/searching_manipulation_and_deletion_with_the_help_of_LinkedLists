class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedLists:
    def __init__(self):
        self.head=None
    def push(self,data):
        New_node=node(data)
        if self.head==None:
            self.head=New_node
            return
        New_node.data=data
        New_node.next=self.head
        self.head=New_node

# display element from last with the help of position or index
    def desplay_ele(self,n):
        if self.head.next==None:
            return None
        curr=self.head
        size=0
        while(curr!=None):
            curr=curr.next
            size=size+1
        pre=self.head
        i=1
        index=(size-n)+1
        while(i<=index):
            if i==index:
                print(pre.data)
                break
            i = i + 1
            pre = pre.next

    def display(self):
        curr=self.head
        while(curr!=None):
            print(curr.data , end=" ->")
            curr=curr.next
        print("null")
#count the position of element or data with the help of data
    def counterPos(self,data):
        curr=self.head
        counter=0
        while(curr!=None):
            counter=counter+1
            if curr.data==data:
                break
            curr=curr.next
        print(counter)
#display the data with the help of position start with the linkedlists
    def startwithfirst(self,n):
        curr=self.head
        i=1
        while i<=n:
            if i==n:
                print(curr.data)
                break
            curr=curr.next
            i=i+1
# delete the nth element from the end of the linked lists
    def nthele(self,n):
        if self.head.next==None:
            return None
        curr=self.head
        size=0
        while(curr!=None):
            curr=curr.next
            size=size+1
        pre=self.head
        index=size-n
        i=1
        while(i<index):
            i=i+1
            pre = pre.next
        pre.next=pre.next.next
        return self.head
#delete the data with the help of position from starting of the linkedlists
 
    def dele_start(self,n):
        if n==1:
            self.head.next=None
        curr=self.head
        index=n-1
        i=1
        while(i<index):
            i=i+1
            curr=curr.next
        curr.next=curr.next.next

if __name__=="__main__":
    d=LinkedLists()
    d.push(1)
    d.push(2)
    d.push(3)
    d.push(4)
    d.display()
    d.desplay_ele(2)
    d.startwithfirst(3)