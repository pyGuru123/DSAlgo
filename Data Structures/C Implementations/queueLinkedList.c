// Online C compiler to run C program online

#include <stdio.h>

#include <stdlib.h>

struct Node {

    int data;

    struct Node *next;

} *start = NULL;

int maxsize = 5;

int length = 0;

void Queue(int d) {

    struct Node *temp;

    temp = (struct Node *)malloc(sizeof(struct Node));

    temp->data = d;

    temp->next = NULL;

    if (start == NULL) {

        start = temp;

        printf("Queue Created successfully");

        length = 1;

    }

}

int size() {

    return length;

}

int isEmpty() {

    return size() == 0;

}

void enqueue(int d) {

    struct Node *temp;

    temp = (struct Node *)malloc(sizeof(struct Node));

    temp->data = d;

    temp->next = NULL;

    if (size() < maxsize) {

        temp->next = start;

        start = temp;

        length += 1;

    }

    else {

        printf("Queue overflow");

    }

} 

void dequeue() {

    struct Node *temp, *ptr;

    if (isEmpty()) {

        printf("Queue underflow");

    }

    else {

        ptr = start;

        while (ptr->next->next != NULL) {

            ptr = ptr->next;

        }

        temp = ptr->next;

        ptr->next = NULL;

        printf("Element deleted %d", temp->data);

        free(temp);

        length -= 1;

    }

}

int main(){

    int choice, data=0;

    while (choice!=5) {

        printf("\n1. Create a Queue");

        printf("\n2. Enqueue an element");

        printf("\n3. Dequeue an element");

        printf("\n4. Get Queue Size");

        printf("\n5. Exit");

        

        printf("\n Enter a choice");

        scanf("%d", &choice);

        

        switch(choice) {

            case 1: 

                    printf("Enter a start element : ");

                    scanf("%d", &data);

                    Queue(data);

                    break;

            case 2: 

                    if (start == NULL) {

                        printf("Create a Queue First");

                    }

                    else{

                        printf("Enter a start element : ");

                        scanf("%d", &data);

                        enqueue(data);

                    }

                    break;

            case 3: 

                    dequeue();

                    break;

            case 4: 

                    size();

                    break;

            case 5: break;

            default: break;

        }

    }

}
