l//  Priority Queue as array structure

#include <stdio.h>

// macros
#define maxsize 5

// Function declarations
int isEmpty();
int isFull();
void insert(int, int);
void display();
int queueSize();
int getHighestPriority();
int deleteHighestPriority();

// Global Vars
struct pqueue{
    int data;
    int priority;
} queue[maxsize];

int rear = -1;

int main(){
    int choice=0, element=0, priority=0;
    
    while (1) {
        printf("\n1. Insert Element\n");
        printf("2. Display Queue\n");
        printf("3. Get Highest priority Element\n");
        printf("4. Delete Element\n");
        printf("5. Queue Size\n");
        printf("5. Exit\n");
        
        printf("\nEnter choice : ");
        scanf("%d", &choice);
        
        switch(choice) {
            case 1 : if (!isFull()){
                        printf("Inserting Element : ");
                        scanf("%d", &element);
                        printf("Inserting Priority : ");
                        scanf("%d", &priority);
                        insert(element, priority);
                    }
                    else {
                        printf("Queue Overflow");
                    }
                    break;
            case 2 : if (!isEmpty()) {
                        display();
                    }
                    else {
                        printf("Queue Empty");
                    }
                    break;
            case 3 : if (!isEmpty()) {
                        element, priority = getHighestPriority();
                        printf("data : %d, priority : %d\n", element, priority);
                    }
                    else {
                        printf("Queue Empty");
                    }
                    break;
            case 4 : if (!isEmpty()) {
                       element = deleteHighestPriority();
                        printf("data : %d\n", element); 
                    }
                    else {
                        printf("Queue Empty");
                    }
                    break;
            case 5 : if (!isEmpty()) {
                        printf("Queue Size : %d", queueSize());
                    }
                    else {
                        printf("Queue Empty");
                    }
                    break;
            case 6 : exit(0);
            default: break;
        }
    }
    return 0;
}

int isEmpty() {
    return rear == -1;
}

int isFull() {
    return rear == maxsize - 1;
}

void insert(int d, int p) {
    rear += 1;
    queue[rear].data = d;
    queue[rear].priority = p;
}

void display() {
    printf("Queue : ");
    for (int i=0; i<=rear; i++) {
        printf("(%d, %d) | ", queue[i].data, queue[i].priority);
    }
    printf("\n");
}

int queueSize() {
    return rear+1;
}

int getHighestPriority() {
    int p = -1, d=-1;
    for (int i=0; i<=rear; i++) {
        if (queue[i].priority > p) {
            p = queue[i].priority;
            d = queue[i].data;
        }
    }
    return d, p;
}

int deleteHighestPriority() {
    int p=-1, d=-1, i, j;
    d, p = getHighestPriority();
    for (i=0; i<=rear; i++) {
        if (queue[i].priority == p) {
            d = queue[i].data;
        }
    }
    for (j=i; j<=rear; j++) {
        queue[j].priority = queue[j+1].priority;
        queue[j].data = queue[j+1].data;
    }
    rear -= 1;
    return d;
}