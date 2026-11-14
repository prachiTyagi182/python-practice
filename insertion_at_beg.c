#include<stdio.h>
#include<stdlib.h>
typedef struct list
{
    int INFO;
    struct list *NEXT;
}NODE;
void insertion_at_beg(int**head,int value)
{
    NODE *ptr;
    ptr=malloc(size of(NODE));
    ptr->INFO=value;
    ptr_->NEXT=NULL;
    if (*head==NULL)
    {
        *head=ptr;
    }
    else{
        ptr->NEXT=*head;
        *head=ptr;
    }
}
void display(NODE *h)
if(h==NULL){
printf("\n link list is empty");}
else
while(h!=NULL)
{
printf("%d->",h->INFO)
h=h->NEXT;
}
int main()
{
    NODE=*head;
    head=NULL;
    insertion_at_beg(&head,10);
    insertion_at_beg(&head,20);
    insertion_at_beg(&head,15);
printf("linked list:");
display(h);
return 0;
}