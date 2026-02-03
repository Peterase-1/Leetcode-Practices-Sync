class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for op in operations:
            if '+' in op:
                x+=1
            if '-' in op:
                x-=1

        return x