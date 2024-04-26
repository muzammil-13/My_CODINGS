/*
 ============================================================================
 Name        : ifElse-LargNum.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include<stdio.h>
#include<stdlib.h>

int main(void){
	setbuf(stdout,NULL);
	int num1,num2;
	printf("Enter two numbers:\n");
	scanf("%d%d",&num1,&num2);
	if(num1>num2){
		printf("Greatest number is %d",num1);
	}else{
		printf("Greatest number is %d",num2);
	}
	return 0 ;
}
