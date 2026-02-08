class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                
                right_empty = (i == length - 1 or flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1

                    if n == 0:
                        return True

        return n <= 0
