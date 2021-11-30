public class BubbleSort {
    
    public static void main(String[] args){
        int[] array = {5, 4, 2, 7, 9, 3, 1, 8, 6};
        int [] newArray = Sort(array);
        System.out.println("Sorted Array: ");
        for(int i : newArray){
            System.out.print(i);
        }
    }

    public static int[] Sort(int[] array){
        for(int i = 0; i < array.length - 1; i++){
            for(int j = 0; j < array.length - i - 1; j++){
                if(array[j] > array[j + 1]){
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
        return array;
    }

}
