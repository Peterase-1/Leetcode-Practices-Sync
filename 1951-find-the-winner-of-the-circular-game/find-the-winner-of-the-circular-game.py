class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        winner = 0
        for total_friends in range(2, n + 1):
            winner = (winner + k) % total_friends
        return winner + 1