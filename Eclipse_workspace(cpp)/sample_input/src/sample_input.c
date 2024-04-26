/*
 ============================================================================
 Name        : sample_input.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include<stdio.h>

int main(void){
	setbuf(stdout,NULL);
	int a;
	printf("Enter a number:");
	scanf("%d",&a);
	printf("You have entered %d",a);

	return 0;
}
;
