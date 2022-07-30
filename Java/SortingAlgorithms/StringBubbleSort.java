package SortingAlgorithms;
public class StringBubbleSort{

    public static void main(String[] args){
        int[] array = {8,7,5,1,3,2,6,9,4};
        Sort(array);

        //Here the main-Method already does the job of iterating through the new array
        // for(int i = 0; i < array.length; i++){
        //     System.out.print(array[i]);
        // }
    }

    public static void Sort(int[] array){
        // String result = "";
        for(int i = 0; i < array.length; i++){
            for(int j = 0; j < array.length - i - 1; j++){
                if(array[j] > array[j + 1]){
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
        // concatenating array-values into a String
        // for(int x = 0; x < array.length; x++){
        //     result += array[x] + " ";
        // }
        // return result;

        //Returning a int[]_value (inefficient due to Call by Reference)
        // return array;

        //in case only the Method is called
        for(int i : array){
            System.out.print(array[i - 1] + " ");
        }
    }
}