class Solution:
    def getSum(self, a: int, b: int) -> int:

        """
            1) Extract LSB by doing right shift by i
            2) Calculate the remainder by doing carry XOR the extracted LSBs 
            3) The result will be an OR of a 1 bit with this calculated remainder, where the result is right shift by i 
            4) The carry should the xor carry and extrracted lsbs 
        """

        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0: 

            carry = (a & b) << 1 
            sum_without_carry = (a ^ b) 

            a = sum_without_carry & mask 
            b = carry & mask 
        

        return a if a < max_int else ~(a ^ mask)

        