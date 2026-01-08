#include <stdio.h>

void insertion_sort(int A[],int n){
    int ch,i,j;
    for (j=1;j<n;j++){
        ch=A[j];
        i=j-1;
        while((i>=0)&&(A[i]>ch)){
            A[i+1]=A[i];
            i=i-1;
        }
        A[i+1]=ch;
    }
    
}

int main(){
    int  vet[5]={7,5,1,8,3};
    insertion_sort(vet,5);
    for(int i=0;i<5;i++){
        printf("%d ",vet[i]);
    }
    return 0;
}