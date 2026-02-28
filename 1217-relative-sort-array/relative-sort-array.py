from collections import Counter

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        dict1 = Counter(arr1)
        soln = []

        for i in arr2:
            soln.extend([i] * dict1[i])
            del dict1[i]  

        for num in sorted(dict1.elements()):
            soln.append(num)

        return soln