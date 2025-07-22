class Solution:
    def reverseDigits(self, n):
        lst =[]
        while(n>0):
            last = n%10
            lst.insert(0,last)
            n = n//10
        sum =0
        for i in range(0,len(lst)):
            sum = sum+ (lst[i]*(pow(10,i)))
        return sum