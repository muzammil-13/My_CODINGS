/*
 ============================================================================
 Name        : arrayLimit.c
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
	int a[100];
	int i,limit;

	printf("Enter the Array size:\n");
	scanf("%d",&limit);

	printf("Enter array values:\n");
	for(i=0;i<limit;i++){
		scanf("%d",&a[i]);
	}

	printf("Entered values are:\n");
	for(i=0;i<limit;i++){
		printf("%d\n",a[i]);
	}
	return EXIT_SUCCESS;
}
