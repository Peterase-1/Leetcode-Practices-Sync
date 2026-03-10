class Solution(object):
    def frequencySort(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        sorted_chars = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        
        result = ""
        for ch in sorted_chars:
            result += ch * freq[ch]
        
        return result