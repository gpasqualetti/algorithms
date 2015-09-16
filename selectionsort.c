#include <stdio.h>
#include "miscellanea.h"

int main();
void selectionSort(int* a,int n);

int main() {
  int a[5]={5,3,1,4,2};
  int n=5;
  printf("Initial array: ");
  printArray(a,n);
  selectionSort(a,n);
  printSorted(a,n);
}

void selectionSort(int* a, int n) {
  int i,j,curr,tmp;
  for (i=0; i<n; i++) {
    for (j=i+1; j<n; j++) {
      if (a[j]<a[i])
	swap(a,j,i);
    }  
  }
}
	  
	
