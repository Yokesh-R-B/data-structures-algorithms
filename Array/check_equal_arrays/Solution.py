class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        
        check = {}
        
        for x in a:
            check[x] = check.get(x,0) + 1
            
        for y in b:
            if(y not in check):
                return False
            
            check[y] -=1
            
            if(check[y] < 0):
                return False
        
        return True