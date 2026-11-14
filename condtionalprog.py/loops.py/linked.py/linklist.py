class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
        
    def __len__(self):
        return self.n
    
    def append(self, value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
            
        self.n += 1
        
    def prepend(self, value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
        self.n += 1


    #delete first node
    def delete_head(self):    

        if self.head is None:
            return
        self.head=self.head.next
        self.n -=1 
    #delete last node\
    def delete_tail(self):
        
        if self.head is None:
            return
        curr=self.head
        while curr.next.next:#yeh none se pehle ka pehla dega    
          curr=curr.next
        curr.next=None    
        curr.n -=1
    #delete by value
    def remove(self,value):
        
        if self.head is None:
            return   
        if self.head.data==value:
            self.head.data=self.head.next    
            
            
        curr=self.head

        while curr.next:
         if curr.next.data==value:#check krga ki curr.next mein joh data hai woh kya humari given value ke equal hai
           break
        curr=curr.next

        if curr.next is None:
            print("value not found")
            return

        curr.next=curr.next.next    
        self.n -=1

    #search
    def search(self,value):    
        curr=self.head#joh hum value denge usko search krga and phir uska indexx return krga
        pos=0
        while curr:#yeh none tk check krga and yeh last tk check krga and jb self.head.data =value ho jayega uski pos return
            if curr.data==value:
             return pos
            curr=curr.next#yeh jb chla jaise suppose value match nhi hui toh woh curr ko curr.next de deddga
            pos+=1#sath mein position ko bhi increment krdega

        return -1
    
    #reverse
    def reverse(self):
        prev=None#taaki humara data loose na ho
        # curr=self.head current node ko track krne ke liye
        while curr:
            nxt=curr.next#ek temporray variable joh curr.next ki value store krga
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev
#middle node
    def middle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
          slow=slow.next #slow ek time mein ek hi baar iterate ho rha hai   

          fast=fast.next.next#yeh one step aage hota hai 
        return slow.data if slow else None
    
#remove duplicates
    def remove_duplicates(self):    
        curr=self.head
        while curr and curr.next:
            if curr.data==curr.next.data:
                curr.next=curr.next.next
                self.n -=1
            else:
                curr=curr.next    