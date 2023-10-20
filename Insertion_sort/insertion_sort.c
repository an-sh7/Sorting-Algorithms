#include<stdio.h>

int main(){
    int list[] = {2,5,3,63,36,34,25,72};
    int n = sizeof(list)/sizeof(list[0]);
    int key = 0;

    for (int i = 0; i < n ;i++){
        key = list[i];
        int j = i - 1;

        while (j >= 0 && key < list[j])
        {
            list[j+1] = list[j];
            j -= 1;
        }
        list[j+1] = key;
    }
    for (int i = 0; i < n; i++)
    {
        printf("%d\n",list[i]);
    }
    
}   