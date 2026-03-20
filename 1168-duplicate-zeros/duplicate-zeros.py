class Solution(object):
    def duplicateZeros(self, arr):
        n = len(arr)
        i = 0

        while i < n:
            if arr[i] == 0:
                for j in range(n - 1, i, -1):
                    arr[j] = arr[j - 1]
                i += 1
            i += 1