class Solution:
    def sort012(self, arr):
        # code here
        zero=0
        one=0
        two=0
        for x in arr:
            if(x==0):
                zero+=1
            if(x==1):
                one+=1
            if(x==2):
                two+=1
                
        for i in range(0,zero):
            arr[i]=0
        for i in range(zero,zero+one):
            arr[i]=1
        for i in range(zero+one,zero+one+two):
            arr[i]=2
        
        return arr