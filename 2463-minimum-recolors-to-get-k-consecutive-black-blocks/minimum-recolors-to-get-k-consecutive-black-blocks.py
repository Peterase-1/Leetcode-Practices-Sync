class Solution(object):
    def minimumRecolors(self, blocks, k):
        whites = blocks[:k].count('W')
        min_ops = whites
        
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                whites -= 1
            
            if blocks[i] == 'W':
                whites += 1
            
            min_ops = min(min_ops, whites)
        
        return min_ops