class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest = max(strs)
        smallest = min(strs)


        for i in range(len(smallest)):
            if(smallest[i]!=longest[i]):
                return smallest[:i]

        return smallest
        