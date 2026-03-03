class Solution(object):
    def twoSum(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left < right:
            current_sum = arr[left] + arr[right]

            if current_sum == target:
                return left+1,right+1

            elif current_sum < target:
                left += 1

            else:
                right -= 1