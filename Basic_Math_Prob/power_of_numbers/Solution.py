class Solution:
    def reverseexponentiation(self, n):
        # code here
        actual_n=n
        reverse = 0
        while n>0:
            d = (reverse*10) + n%10
            n//=10
        return actual_n**d