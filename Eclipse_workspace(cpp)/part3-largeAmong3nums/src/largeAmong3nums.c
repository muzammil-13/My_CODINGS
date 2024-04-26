/*
 ============================================================================
 Name        : largeAmong3nums.c
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
	int num1,num2,num3;
	printf("Enter 3 numbers:");
	scanf("%d%d%d",&num1,&num2,&num3);
	if (num1 > num2) {
	        if (num1 > num3) { //nested loop
	            printf("First number ie, %d is greater", num1);
	        } else {
	            printf("Third number ie, %d is greater", num3);
	        }
	} else {
	        if (num2 > num3) { //nested loop
	            printf("Second number ie, %d is greater", num2);
	        } else {
	            printf("Third number ie, %d is greater", num3);
	        }
	    }
	    return EXIT_SUCCESS;
	}
