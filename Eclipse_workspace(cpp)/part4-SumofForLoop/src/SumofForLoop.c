/*
 ============================================================================
 Name        : SumofForLoop.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int main(void) {
	setbuf(stdout,NULL);
	int i,limit,sum=0;
	printf("Enter the limit:");
	scanf("%d",&limit);
	for(i=1;i<limit;i++){
		sum=sum+i;
//		printf("result till now = %d \n",sum);
	}
	printf("SUM = %d \n",sum);
	return EXIT_SUCCESS;
}
