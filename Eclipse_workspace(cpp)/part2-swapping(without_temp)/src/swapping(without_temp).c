/*
 ============================================================================
 Name        : swapping(without_temp).c
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
	int a=10,b=20;

	a=a+b;
	b=a-b;
	a=a-b;

	printf("a=%d, b=%d",a,b);
	return EXIT_SUCCESS;
}
