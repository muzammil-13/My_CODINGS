#include<stdio.h>
#include<stdlib.h>

int main(void){
    setbuf(stdout,NULL);
    
    int i,j;
    for(i=0;i<5;i++){
        for(j=0;j<5;j++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
