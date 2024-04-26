/*
 ============================================================================
 Name        : arrayInput-sample.c
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
	int i,arr[5];

	for(i=0;i<5;i++){
		scanf("%d",&arr[i]);
	}
	printf("array inputs are:%d\n",arr[i]);
	return EXIT_SUCCESS;
}
