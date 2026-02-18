class Solution:
    def intersectSize(self,a, b):
        # code here
        
        d = {}
        inter = 0
        for x in a:
            d[x] = d.get(x,0) + 1
            
        for y in b:
            d[y] = d.get(y,0) + 1
            
        for n,m in d.items():
            if(m>1):
                inter+=1
        
        
        return inter
