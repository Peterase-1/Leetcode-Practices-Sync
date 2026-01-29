class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Finds the longest common prefix string amongst an array of strings using 
        the vertical scanning method.
        
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        first_string = strs[0]
        
        for i in range(len(first_string)):
            char = first_string[i]
            
            for j in range(1, len(strs)):
                current_string = strs[j]
                
                
                if i == len(current_string) or current_string[i] != char:

                    return first_string[:i]

        return first_string