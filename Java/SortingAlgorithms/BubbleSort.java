package SortingAlgorithms;
public class BubbleSort {
    
    public static void main(String[] args){
        int[] array = {5, 4, 2, 7, 9, 3, 1, 8, 6, 15, 20, 13, 230, 3513, 23, 1234, 53};
        Sort(array);
        for(int i : array){
            System.out.print(i + " ");
        }
    }

    public static void Sort(int[] array){
        for(int i = 0; i < array.length - 1; i++){
            for(int j = 0; j < array.length - i - 1; j++){
                if(array[j] > array[j + 1]){
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }
}
