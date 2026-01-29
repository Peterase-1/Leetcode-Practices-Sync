class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Finds the longest common prefix string amongst an array of strings using 
        the vertical scanning method.
        
        :type strs: List[str]
        :rtype: str
        """
        # Edge case: If the input list is empty, there is no common prefix.
        if not strs:
            return ""

        # Use the first string as the reference for comparison.
        first_string = strs[0]
        
        # Iterate through the characters of the first string.
        for i in range(len(first_string)):
            # The character we are comparing against.
            char = first_string[i]
            
            # Now, iterate through the rest of the strings (starting from index 1).
            for j in range(1, len(strs)):
                current_string = strs[j]
                
                # Check for two conditions:
                # 1. If the current string is shorter than the current index 'i'.
                # 2. If the character at index 'i' in the current string does not match 
                #    the character from the first string.
                if i == len(current_string) or current_string[i] != char:
                    # If a mismatch or end-of-string is found, 
                    # the common prefix is the substring of the first string up to index i.
                    return first_string[:i]

        # If the outer loop completes without returning, it means the entire 
        # first string is the common prefix (all strings start with it).
        return first_string