/*
 ============================================================================
 Name        : continue-sample.c
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

	for(i=0;i<7;i++){
		printf("Hi\n");
		if(i==5){
			continue;
		}
		printf("Hello\n");
	}
	printf("Finished\n");
	return EXIT_SUCCESS;
}
