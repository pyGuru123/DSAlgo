// Circular Queue

#include <stdio.h>

// macros
#define maxsize 5

// function declarations
void insert(int);
void display();
int isEmpty();


// Global Variables
int front=-1, rear=-1;
int arr[maxsize];

// Main Function
int main(){
    int choice=0, element=0;
    while (1) {
        printf("1. Insert Element\n");
        printf("2. Display Queue\n");
        printf("3. Delete Element\n");
        printf("4. Queue Size\n");
        printf("5. Exit\n");
        
        printf("\nEnter choice : ");
        scanf("%d", &choice);
        
        switch(choice) {
            case 1 : printf("Insert Data : ");
                     scanf("%d", &element);
                     insert(element);
            case 2 : display();
                     break;
            case 3 : break;
            case 4 : break;
            case 5 : exit(0);
                     break;
            default: break;
        }
    }
}

int isEmpty() {
    return rear == -1;
}

// Function Definitions
void insert(int ele) {
    if (front == -1) {
        front = rear = 0;
    }
    
    if (rear == maxsize - 1){
        rear = 0;
    }
    else {
        rear += 1;
    }
    
    arr[rear] = ele;
}

void display() {
    for (int i=0; i<=maxsize-1; i++) {
        printf("%d", arr[i]);
    }
}