/*
 ============================================================================
 Name        : switchSample.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include<stdio.h>
#include<stdlib.h>

int main(){
	setbuf(stdout,NULL);
	int choice;
	printf("Choose from FOOD MENU:\n > 1.Porotta \n > 2.Biriyani \n > 3.Fried Rice \n > 4.Mandthi \n");
	scanf("%d",&choice);
	printf("You have selected ");
	switch(choice){
	case 1:
		printf("Porotta");
		break;
	case 2:
		printf("Biriyani");
		break;
	case 3:
		printf("Fried Rice");
		break;
	case 4:
		printf("Mandhi");
		break;
	default:
		printf("NO FOOD FROM MENU");
	}
	return 0;
}
