class Solution(object):
    def predictTheWinner(self, nums):
        
        def play(left, right, score1, score2, turn):
            if left > right:
                return score1 >= score2
            
            if turn == 1:  
                return (
                    play(left + 1, right, score1 + nums[left], score2, 2) or
                    play(left, right - 1, score1 + nums[right], score2, 2)
                )
            else: 
                return (
                    play(left + 1, right, score1, score2 + nums[left], 1) and
                    play(left, right - 1, score1, score2 + nums[right], 1)
                )
        
        return play(0, len(nums) - 1, 0, 0, 1)