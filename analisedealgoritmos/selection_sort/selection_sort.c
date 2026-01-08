#include <stdio.h>

void selection_sort(int A[], int n)
{
    int min_index, i, j, aux;
    for (j = 0; j < n - 1; j++)
    {
        min_index = j;
        for (i = j + 1; i < n; i++)
        {
            if (A[i] < A[min_index])
                min_index = i;
        }
        if (A[j] > A[min_index])
        {
            aux = A[j];
            A[j] = A[min_index];
            A[min_index] = aux;
        }
    }
}

int main(){
    int vet[5]={7,5,1,8,3};
    selection_sort(vet,6);
    for(int i=0;i<5;i++){
        printf("%d ",vet[i]);
    }

}