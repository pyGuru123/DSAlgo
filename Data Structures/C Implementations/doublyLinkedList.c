// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *prev;
    struct Node *next;
} *start = NULL;

void createList(int d) {
    struct Node *temp;
    temp = (struct Node *)malloc(sizeof(struct Node));
    temp->data = d;
    temp->next = NULL;
    temp->prev = NULL;
    if (start == NULL) {
        start = temp;
    }
}3


void insertBeg(int d){
    struct Node *temp;
    temp = (struct Node *)malloc(sizeof(struct Node));
    temp->data = d;
    temp->next = NULL;
    temp->prev = NULL;
    if (start == NULL) {
        start = temp;
    }
    else {
        temp->next = start;
        start->prev = temp;
        start = temp;
    }
}

void displayList(){
    struct Node *ptr;
    ptr = start;
    while(ptr!= NULL) {
        printf("%d -> ", ptr->data);
        ptr = ptr->next;
    }
}

int main() {
    int choice=0, data=0;
    while (choice != 9) {
        printf("\n1. Create A Doubly Linked List");
        printf("\n2. Display List");
        printf("\n3. Insert Element at Beg");
        printf("\n4. Insert Element at End");
        printf("\n5. Get List Length");
        printf("\n6. Delete from Beg");
        printf("\n7. Delete from End");
        printf("\n9. Exit");
        
        printf("\nEnter choice : ");
        scanf("%d", &choice);
        
        switch(choice) {
            case 1: 
                    printf("\nInsert Head Element : ");
                    scanf("%d", &data);
                    createList(data);
                    break;
            case 2: 
                    displayList();
                    break;
            case 3: 
                    // printf("\nInsert Element : ");
                    // scanf("%d", &data);
                    // insertBeg(data);
                    break;
            case 4: 
                    // printf("\nInsert Element : ");
                    // scanf("%d", &data);
                    // insertEnd(data);
                    break;
            case 5:
                    // listLength();
                    break;
            case 6:
                    // popBeg();
                    break;
            case 7: 
                    // popEnd();
                    break;
            case 9: break;
            default: break;
        }
    }
    return 0;
}