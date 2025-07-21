class Solution:
    def evenlyDivides(self, n):
        
        count = 0
        actual_n = n
        while (n>0):
            last = n%10
            if last!=0 and actual_n%last==0:
                count+=1
            n=n//10
        
        return count 