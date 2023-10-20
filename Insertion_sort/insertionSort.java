public class insertionSort {
    public static void main(String[] args) {
        int list[] = {2,56,23,673,23,5572,563};
        int key,j = 0;
        for (int i = 0; i < list.length; i++) {
            key = list[i];
            j = i - 1;

            while (j >= 0 && key < list[j]) {
                list[j + 1] = list[j];
                j -= 1;
            }
            list[j+1] = key;
        }
        for (int i = 0; i < list.length; i++) {
            System.out.println(list[i]);
        }
    }
    
}