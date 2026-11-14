class Node:
    def __init__(self,data):#init is an initialization function
        self.data=data#node ke andr ki value
        self.next=None#next node ka address

# def reverse(head):
#         prev=None#taaki humara data loose na ho
#         curr=head# current node ko track krne ke liye
#         while curr:
#             nxt=curr.next#ek temporray variable joh curr.next ki value store krga
#             curr.next=prev
#             prev=curr
#             curr=nxt
#         return prev

def number(head):#starting point of the node jaha se hum curr mein value daalmnge and usko num mein store krayenge
        num=0
        #humne joh head bnaya hai usko hum current mein assign krayenge aur humara curr ab node ke start pr hai
        curr=head#hr node ke pass apna data and next node ka address bhi addfred hota hai but
        #yeh necessay nhi ki he node ke pass head ho isliye hum yaha self.head nhi likhnge
        while curr:#yeh jbtk chlga jbtk curr ki value None nhi hoti
            #2->3->3
          num=(num*10)+curr.data #curr abhi head pr hai curr.data=2 num=(0*10)=2=2
          #num=(2*10)+3=23 
          # num=(23*10)+3=233  
          curr=curr.next
        return num 
    
head=Node(2) #starting node mein   
head.next=Node(3)#starting node ka next node
head.next.next=Node(3)#next to next node
# reverselist=reverse(head)
print(number(head))

