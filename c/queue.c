#include<stdio.h>
#include<stdbool.h>
#define capacity 5

int ourQueue[capacity];
int front = 0, rear = -1, totalItem = 0;

bool isFull(){
    if (totalItem == capacity){
        return true;
    }
    return false;
}

bool isEmpty(){
    if(totalItem == 0){
        return true;
    }
    return false;
}

void enqueue(int item){
    if(isFull()){
        printf("Sorry, the Queue is full.\n");
        return;
    }
    rear = (rear + 1) % capacity;
    ourQueue[rear] = item;
    totalItem++;
}

int dequeue(){
    if(isEmpty()){
        printf("Sorry, The Queue is empty. \n");
        return -1;
    }
    int frontItem = ourQueue[front];
    ourQueue[front] = -1;
    front = (front + 1) % capacity;
    totalItem = totalItem -1;
    totalItem--;
    return frontItem;
}

void printQueue(){
    int i;
    printf("Queue: ");
    for ( i = 0; i < capacity; i++)
    {
        printf("%d ", ourQueue[i]);
    }
    printf("\n");
    
}

int main(){
    enqueue(30);
    enqueue(80);
    enqueue(40);
    enqueue(50);
    enqueue(40);
    printQueue();
    enqueue(50);
    printQueue();
    printf("Deque: %d\n", dequeue());
    printQueue();
    enqueue(100);
    printQueue();
    return 0;
}