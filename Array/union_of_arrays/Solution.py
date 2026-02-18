class Solution:    
    def findUnion(self, a, b):
        # code here
        
        s = set()
        
        for x in a:
            s.add(x)
        for y in b:
            s.add(y)
            
        return(list(s))
            