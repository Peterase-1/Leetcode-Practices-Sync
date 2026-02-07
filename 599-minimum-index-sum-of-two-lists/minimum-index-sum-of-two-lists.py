class Solution(object):
    def findRestaurant(self, list1, list2):

        minindex = []
        sumIndex = float('inf')

        for i in list1:
            if i in list2:

                index_sum = list1.index(i) + list2.index(i)

                if index_sum < sumIndex:
                    sumIndex = index_sum
                    minindex = [i]

                elif index_sum == sumIndex:
                    minindex.append(i)

        return minindex
