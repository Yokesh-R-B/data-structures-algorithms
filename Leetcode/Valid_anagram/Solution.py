class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        check = {}
        if(len(s)!=len(t)):
            return False
        for x in s:
            check[x] = check.get(x,0) + 1
        
        for y in t:
            check[y] = check.get(y,0) - 1
            if(check[y] < 0):
                return False
        return True  