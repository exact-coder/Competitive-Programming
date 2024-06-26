#include<stdio.h>

int main(){
    int x ;
    x = 10;
    int *ptr;
    ptr = &x;

    printf("%d\n", x);

    printf("%p\n", &x);

    printf("%p\n", ptr);

    

    return 0;
}
