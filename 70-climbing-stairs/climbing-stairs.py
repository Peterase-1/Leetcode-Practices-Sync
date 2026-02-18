class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1,2]
        
        for i in range(2,n):
            # ans[i]= ans[i-1]+ans[i-2]
            ans.append(ans[i-1]+ans[i-2])
        return ans[n-1]