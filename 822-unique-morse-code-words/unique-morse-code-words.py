class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        alp = "abcdefghijklmnopqrstuvwxyz"
        ans = []
        for word in words:
            stmor = ""
            for i in word:
                stmor+=  morse[alp.index(i)]
            ans.append(stmor)

        return len(set(ans))