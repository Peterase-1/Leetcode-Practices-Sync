from collections import defaultdict

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        lossCount = defaultdict(int)
        players = set()
        
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            lossCount[loser] += 1
        
        allWin = [player for player in players if player not in lossCount]
        oneLoss = [player for player, count in lossCount.items() if count == 1]
        
        return [sorted(allWin), sorted(oneLoss)]
