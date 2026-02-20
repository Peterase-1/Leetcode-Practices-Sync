from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        
        paragraph = re.sub(r'[^a-z]', ' ', paragraph)
        
        words = paragraph.split()
        
        banned_set = set(banned)
        word_count = Counter()
        
        for word in words:
            if word not in banned_set:
                word_count[word] += 1
        
        return word_count.most_common(1)[0][0]