/*
 ============================================================================
 Name        : sumof2nums.c
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
	int num1,num2,sum;
	printf("Enter 2 numbers:");
	scanf("%d%d",&num1,&num2);
	sum=num1+num2;
	printf("Sum of two numbers = %d",sum);

	return EXIT_SUCCESS;
}
