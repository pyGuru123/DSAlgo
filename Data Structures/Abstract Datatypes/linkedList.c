// Online C compiler to run C program online

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};
struct Node *head = NULL;
int data=0;

void createList(int d) {
    struct Node *temp;
    temp = (struct Node *)malloc(sizeof(struct Node));
    temp->data = d;
    temp->next = NULL;
    
    if (head == NULL) {
        head = temp;
    }
}

void displayList(){
    struct Node *ptr;
    ptr = head;
    while (ptr != NULL) {
        printf("%d ->", ptr->data);
        ptr = ptr->next;
    }
}

void insertBeg(int d) {
    struct Node *temp;
    temp = (struct Node *)malloc(sizeof(struct Node));
    temp->data = d;
    temp->next = NULL;
    
    if (head == NULL) {
        head = temp;
    }
    else {
        temp->next = head;
        head = temp;
    }
}

void insertEnd(int d) {
    struct Node *temp, *ptr;
    temp = (struct Node *)malloc(sizeof(struct Node));
    temp->data = d;
    temp->next = NULL;
    
    ptr = head;
    while (ptr->next != NULL) {
        ptr = ptr->next;
    }
    ptr->next = temp;
}

void listLength(){
    int length=0;
    struct Node *ptr;
    ptr = head;
    while (ptr != NULL) {
        length += 1;
        ptr = ptr->next;
    }
    printf("\nLength of the list : %d", length);
}

void popBeg() {
    struct Node *temp;
    if (head != NULL) {
        temp = head;
        head = head->next;
        printf("\nElement Deleted %d", temp->data);
        free(temp);
    }
    else {
        printf("Empty List");
    }
}

void popEnd() {
    struct Node *ptr, *temp;
    if (head != NULL) {
        ptr = head;
        while (ptr->next->next != NULL) {
            ptr = ptr->next;
        }
        temp = ptr->next;
        ptr->next = NULL;
        printf("Element Deleted : %d", temp->data);
        free(temp);
    }
}

int main() {
    int choice=0;
    while (choice != 9) {
        printf("\n1. Create A Linked List");
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
                    printf("\nInsert Element : ");
                    scanf("%d", &data);
                    insertBeg(data);
                    break;
            case 4: 
                    printf("\nInsert Element : ");
                    scanf("%d", &data);
                    insertEnd(data);
                    break;
            case 5:
                    listLength();
                    break;
            case 6:
                    popBeg();
                    break;
            case 7: 
                    popEnd();
                    break;
            case 9: break;
            default: break;
        }
    }
    return 0;
}