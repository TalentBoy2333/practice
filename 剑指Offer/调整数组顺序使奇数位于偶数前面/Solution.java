public class Solution {
    public void reOrderArray(int [] array) {
        int ou[] = new int[array.length];
        int ouInd = 0;
        int jiInd = 0;
        for(int i = 0; i < array.length; i++){
            if(array[i] % 2 == 1){
                array[jiInd++] = array[i];
            }else{
                ou[ouInd++] = array[i];
            }
        }
        for(int i = 0; i < ouInd; i++){
            array[jiInd++] = ou[i];
        }
    }
}