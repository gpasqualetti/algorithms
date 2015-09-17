#include <stdio.h>
#include "miscellanea.h"

/* I want to know the ith min element of an unordered array */

void main();
int quickSelect(int* a, int l, int r, int k);
int partitionate(int* a, int l, int r, int k);

void main() {
  int a[5]={4,2,7,6,1};
  int n=5;
  int i=5;
  int x=quickSelect(a,0,n,i);
  printf("The nr %i min element of the array is %i.",i,x);
  putchar('\n');
}

int partitionate(int* a, int l, int r, int k) {
  int p=a[l];
  int i=l+1,j;
  for (j=l+1;j<=r;j++) {
    if (a[j]<a[l]) {
	swap(a,j,i);
	i++;
      }
  }
  swap(a,l,i-1);
  return i-1;
}

int quickSelect(int* a, int l, int r, int k) {
  if (l==r)
    return a[l];
  int p=partitionate(a,l,r,k);
  if (k-1==p)
    return a[p];
  else if (k-1<p)
    return quickSelect(a,l,p-1,k);
  else
    return quickSelect(a,p+1,r,k);
}
  
  
	
	      
