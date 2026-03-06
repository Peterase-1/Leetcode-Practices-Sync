class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        res = []
        n = len(arr)
        def flip(k):
            arr[:k] = arr[:k][::-1]

        for size in range(n,1,-1):
            max_index = arr.index(size)

            if max_index != size-1:
                if max_index!=0:
                    res.append(max_index+1)
                    flip(max_index + 1)

                res.append(size)
                flip(size)

        return res