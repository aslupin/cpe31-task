#include <stdio.h>
int main(){
    int c[] = {1,2,3,4};
    int *p;
    p = c[1];
   //' p += 2;
    printf("%d %d %d %d",*p,p,&p,&c[0],&c[1]);
}