/*In bubble sort we compare the first two elements and then switch them according to the value*/


public class bubbleSort {
    public static void main(String[] args) {
        int list[] = {2, 4, 62, 25, 6, 36, 52};
        int n = list.length;
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (list[j] > list[j + 1]) {
                    // Swap list[j] and list[j + 1]
                    int temp = list[j];
                    list[j] = list[j + 1];
                    list[j + 1] = temp;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            System.out.println(list[i]);
        }
    }
}




