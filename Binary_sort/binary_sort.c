#include<stdio.h>
#include<time.h>
int binary_search(int target,int arr[],int size){
    int first = 0;
    int last = size - 1;
    
    while (first <= last)
    {
        int midpoint = (first + last)/2;
        if (arr[midpoint] == target){
            return midpoint;
        }else if(arr[midpoint] < target){
            first = midpoint + 1;
        }else
        {
            last = midpoint - 1;
        }
        
    }
    printf("Value is not in the list");
}
int main(){
    int arr[] = {1, 2, 4, 5, 6, 7, 8, 10, 34, 65, 76};
    int target = 34;
    int size = sizeof(arr) / sizeof(arr[0]);
    int search = binary_search(target, arr, size);
    printf("%d",search);
}
