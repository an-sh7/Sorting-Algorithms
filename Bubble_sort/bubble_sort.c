#include<stdio.h>
void main(){
    int list[] = {2,35,32,5,1,43,523};
    int n = sizeof(list)/sizeof(list[0]);
    
    for (int i = 0; i < n - 1;i++){
        for (int j = 0;j < n -i -1;j++){
            if (list[j] > list[j + 1]){
                int temp = list[j];
                list[j] = list[j+1];
                list[j + 1] = temp;
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        printf("%d\n",list[i]);
    }
    
}