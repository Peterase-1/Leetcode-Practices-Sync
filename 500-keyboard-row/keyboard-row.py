class Solution(object):
    def findWords(self, words):
        r1 = set("qwertyuiop")
        r2 = set("asdfghjkl")
        r3 = set("zxcvbnm")

        ans = []

        for word in words:
            w = word.lower()

            if all(ch in r1 for ch in w) or all(ch in r2 for ch in w) or all(ch in r3 for ch in w):
                ans.append(word)

        return ans
