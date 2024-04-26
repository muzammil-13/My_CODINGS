/*
 ============================================================================
 Name        : ifElse.c
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
		int num;
		printf("Enter a number:");
		scanf("%d",&num);
		if(num<0){
			printf("Entered number is negative!");
		}else{
				printf("Entered number is positive");
		}
	return EXIT_SUCCESS;
}
