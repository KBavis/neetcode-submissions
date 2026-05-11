class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0
        
        # 32 bit integer 
        for i in range(32):

            # take the least significant bit in n, perform & operator with 1
            bit = (n >> i) & 1 

            # add bit to res in reverse order (shift extracted bit to left 31 - i times)
            res += (bit << (31 - i))
        
        return res
