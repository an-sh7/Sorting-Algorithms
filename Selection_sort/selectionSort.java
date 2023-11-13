public class selectionSort {
    public static void main(String[] args) {
        int[] array = {34, 52, 41, 31, 643, 24};
        System.out.print("Unsorted Array is: ");
        printArray(array);
        selection_Sort(array);
        System.out.print("Sorted Array is: ");
        printArray(array);
    }

    public static void selection_Sort(int[] array) {
        int length = array.length;

        for (int i = 0; i < length - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < length; j++) {
                if (array[j] < array[minIndex]) {
                    minIndex = j;
                }
            }

            // Swap the found minimum element with the first element
            int temp = array[i];
            array[i] = array[minIndex];
            array[minIndex] = temp;
        }
    }

    public static void printArray(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }
}
