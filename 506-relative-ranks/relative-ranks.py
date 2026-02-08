class Solution(object):
    def findRelativeRanks(self, score):
        n = len(score)

        answer = [""] * n

        sorted_scores = sorted(score, reverse=True)

        for i in range(n):
            rank = sorted_scores.index(score[i])
            if rank == 0:
                answer[i] = "Gold Medal"
            elif rank == 1:
                answer[i] = "Silver Medal"
            elif rank == 2:
                answer[i] = "Bronze Medal"
            else:
                answer[i] = str(rank + 1)

        return answer
