/*
 ============================================================================
 Name        : primeNum-flagBreak.c
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
	int i,n,flag=0;
	printf("Enter a number:");
	scanf("%d",&n);
	for(i=2;i<n/2;i++){
		if(n%i==0){
			flag=1;
			break;
		}
	}
	if(flag==0){
		printf("%d is a Prime number",n);
	}else{
		printf("%d is Not a Prime",n);
	}
	return EXIT_SUCCESS;
}
