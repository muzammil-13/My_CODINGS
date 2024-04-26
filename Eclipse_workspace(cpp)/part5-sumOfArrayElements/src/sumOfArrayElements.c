/*
 ============================================================================
 Name        : sumOfArrayElements.c
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
	int limit,i,values[100],sum=0;
	printf("Enter limit:");
	scanf("%d",&limit);

	printf("Enter values:");
	for(i=0;i<limit;i++){
		scanf("%d",&values[i]);
	}
	for(i=0;i<limit;i++){
		sum=sum+values[i];
	}
	printf("Result=%d",sum);
	return EXIT_SUCCESS;
}
