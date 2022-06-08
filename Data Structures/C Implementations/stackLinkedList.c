// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>

int maxsize = 5;

struct Node {
    int data;
    struct Node *next;
} *start = NULL;

int isEmpty(){
    return start == NULL;
}

int size(){
    struct Node *ptr;
    int len=0;
    if (!isEmpty()){
        ptr = start;
        while (ptr != NULL){
            len += 1;
            ptr = ptr->next;
        }
    }
    return len;
}

void push(int d) {
    struct Node *temp, *ptr;
    temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = d;
    temp->next = NULL;
    
    if (size() < maxsize) {
        if (start == NULL) {
        start = temp;
        }
        else {
            ptr = start;
            while (ptr->next != NULL) {
                ptr = ptr->next;
            }
            ptr->next = temp;
        }
    }
    else {
        printf("stack overflow");
    }
}

void pop() {
    struct Node *ptr, *temp;
    if (start != NULL) {
        ptr = start;
        while (ptr->next->next != NULL) {
            ptr = ptr->next;
        }
        temp = ptr->next;
        ptr->next = NULL;
        printf("element popped is %d :", temp->data);
        free(temp);
    }
    else {
        printf("Stack underflow");
    }
}

void displayStack(){
    struct Node *ptr;
    ptr = start;
    while (ptr != NULL) {
        printf("%d ->", ptr->data);
        ptr = ptr->next;
    }
}

int main(){
    int choice=0, data=0;
    while (choice != 5) {
        printf("\n1. Push element");
        printf("\n2. Pop element");
        printf("\n3. Display Stack");
        printf("\n4. Get stack size");
        printf("\n5. Exit");
        
        printf("\nEnter choice : ");
        scanf("%d", &choice);
        
        switch(choice) {
            case 1: 
                    printf("\nInsert Head Element : ");
                    scanf("%d", &data);
                    push(data);
                    break;
            case 2: 
                    pop();
                    break;
            case 3: 
                    displayStack();
                    break;
            case 4: 
                    printf("stack has %d elements", size());
                    break;
            case 5:
                    break;
            default: break;
        }
    }
    return 0;
}