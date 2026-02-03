from collections import Counter
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common_count = Counter(words[0])
        
        for word in words[1:]:
            common_count &= Counter(word)
        
        result = list(common_count.elements())
        return result
            
