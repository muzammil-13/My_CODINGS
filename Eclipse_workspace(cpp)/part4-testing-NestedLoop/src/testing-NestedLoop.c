/*
 ============================================================================
 Name        : testing-NestedLoop.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Nested loop in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int main(void) {
	setbuf(stdout,NULL);
	int n,i,j;
	printf("Enter value for n:");
	scanf("%d",&n);

	for(i=1;i<=n;i++){

		for(j=0;j<i;j++){
			printf("\n > Now in nested loop");
		}
	printf("\n");
	printf(">> Exited nested loop.>>> Now in MAIN LOOP");
	}
	return EXIT_SUCCESS;
}
