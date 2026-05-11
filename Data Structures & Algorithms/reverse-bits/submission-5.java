class Solution {
    public int reverseBits(int n) {
        
        int res = 0;

        for (int i = 0; i < 32; i++) {

            // extract LSB 
            int lsb = (n >> i) & 1;

            // perform add at MSB 
            res += (lsb << (31 - i));
        }

        return res;
    }
}
