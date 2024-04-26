/*
 ============================================================================
 Name        : ElseIf-MathematicsChoice.c
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
	int num1,num2,result,choice;
	printf("Enter two numbers:");
	scanf("%d%d",&num1,&num2);
	printf("Choose which operation to be done,\n");
	printf("> 1.Addition \n> 2.Subtraction \n> 3.Multiplication \n> 4.Division\n");
	scanf("%d",&choice);
	if(choice==1){
		result=num1+num2;
		printf("Result=%d",result);
	}else if(choice==2){
		result=num1-num2;
		printf("Result=%d",result);
	}else if(choice==3){
		result=num1*num2;
		printf("Result=%d",result);
	}else if(choice==4){
		result=num1/num2;
		printf("Result=%d",result);
	}else{
		printf("ERROR INPUT GIVEN!");
	}
	return EXIT_SUCCESS;
}
