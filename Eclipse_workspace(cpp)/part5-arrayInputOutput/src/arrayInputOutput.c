/*
 ============================================================================
 Name        : arrayInputOutput.c
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

	int a[5];
	int i;
	printf("Enter values:\n");
	for(i=0;i<5;i++){
		scanf("%d",&a[i]);
	}
	printf("Entered values are:\n");
	for(i=0;i<5;i++){
		printf("%d\n",a[i]);
	}
	return EXIT_SUCCESS;
}
