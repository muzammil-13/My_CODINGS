/*
 ============================================================================
 Name        : part6-Function(withoutArgs,withReturnVal).c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int sum();
int main(void) {
	setbuf(stdout,NULL);

	int res;
	res=sum();
	printf("Result=%d",res);

	return EXIT_SUCCESS;
}
int sum(){
	int a,b,result;
	printf("Enter 2 numbers");
	scanf("%d%d",&a,&b);
	result=a+b;
	return result;
}
