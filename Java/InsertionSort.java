public class InsertionSort {
    void sort(int[] array){
        for(int i = 0; i < array.length - 1; i++){
            int j = i + 1;
            int temp = array[j];
            while(j > 0 && temp < array[j - 1]){
                array[j] = array[j - 1];
                j--;
            }
            array[j] = temp;
        }
    }

    public static void main(String[] args){
        int[] array = {12, 11, 13, 4, 2, 8, 9, 6, 20, 15};

        InsertionSort ob = new InsertionSort();
        ob.sort(array);

        for(int i : array){
            System.out.print(i);
            System.out.print(" ");
        }
    }
}