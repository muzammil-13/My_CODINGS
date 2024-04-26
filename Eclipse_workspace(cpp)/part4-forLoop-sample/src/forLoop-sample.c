/*
 ============================================================================
 Name        : forLoop-sample.c
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
	int i;
	for(i=1;i<=100;i++){
		printf("%d\n",i);
	}
	return EXIT_SUCCESS;
}
