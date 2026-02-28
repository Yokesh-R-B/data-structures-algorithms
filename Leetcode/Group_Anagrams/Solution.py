class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        output = {}

        for x in strs:
            temp = "".join(sorted(x))

            if(temp in output):
                output[temp].append(x)
            else:
                output[temp] = [x]
        
        return list(output.values())