void printArray(int* a, int l);
void swap(int*a, int x, int y);
void printSorted(int* a, int l);
  
void printArray(int* a, int l) {
  int i;
  for (i=0;i<l;i++) {
    printf("%i ",a[i]);
      }
  printf("\n");
}


void swap(int*a, int x, int y) {
  int tmp;
  tmp=a[x];
  a[x]=a[y];
  a[y]=tmp;
}

void printSorted(int* a, int l) {
  printf("Sorted array:  ");
  printArray(a, l);
}
