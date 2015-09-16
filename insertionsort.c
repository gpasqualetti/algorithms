#include <stdio.h>
#include "miscellanea.h"

int main();
void insertionSort(int* a, int n);

int main() {
  int n=7;
  int a[7]={7,3,4,5,1,2,6};
  printf("initial array: ");
  printArray(a,n);
  insertionSort(a,n);
  printf("Sorted array:  ");
  printArray(a,n);
}

void insertionSort(int* a, int n) {
  int next,i,j;
  for (i=1; i<n; i++) {
    next=a[i];
    j=i;
    while (j>0 && a[j-1]>next) {
      a[j]=a[j-1];
      a[j-1]=next;
      j--;
    }
  }
}
