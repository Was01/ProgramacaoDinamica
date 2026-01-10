void bubble_sort(int A[],int n){
    int i,j,aux;
    for(j=0;j<n-1;j++){
        for(i=0;i<n-1-j;i++){
            if(A[i]>A[i+1]){
                aux=A[i];
                A[i]=A[i+1];
                A[i+1]=aux;
            }
        }
    }
}
