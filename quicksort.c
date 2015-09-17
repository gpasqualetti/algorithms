#include <stdio.h>
#include "miscellanea.h"

void main();
void quickSort(int* a, int l, int r);
int partitionate(int* a, int l, int r);
void selectPivot(int* a, int l);

void main() {
  int a[5]={5,4,3,1,2};
  int n=5;
  printArray(a,5);
  quickSort(a,0,4);
  printArray(a,5);
}

int partitionate(int* a, int l, int r) {
  int p=a[l];
  int i=l+1,j;
  for (j=l+1;j<=r;j++) {
    if (a[j]<p) {
      swap(a,j,i);
      i++;
    }
  }
  swap(a,l,i-1);
  return i-1;
}

void selectPivot(int* a, int l) {
}

void quickSort(int* a, int l, int r) {
  if ((r-l)<=1)
    return;
  selectPivot(a,l);
  int p=partitionate(a,l,r);
  quickSort(a,l,p-1);
  quickSort(a,p+1,r);
}
