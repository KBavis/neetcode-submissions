class Solution {
    public int getSum(int a, int b) {
        while (b != 0){
            int temp = (a & b) << 1; // carry
            a = a ^ b; // sum w/ out carry 
            b = temp;
        }

        return a;
    }
}
