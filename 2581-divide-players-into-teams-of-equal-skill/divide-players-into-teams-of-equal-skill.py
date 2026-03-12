class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        n = len(skill)
        target = skill[0] + skill[-1]
        total_chemistry = 0
        
        for i in range(n // 2):
            if skill[i] + skill[n-1-i] != target:
                return -1
            total_chemistry += skill[i] * skill[n-1-i]
        
        return total_chemistry