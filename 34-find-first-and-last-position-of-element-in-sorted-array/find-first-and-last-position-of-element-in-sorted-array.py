class Solution(object):
    def searchRange(self, nums, target):
        
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            res = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    res = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return res
        
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            res = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    res = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return res
        
        return [findFirst(nums, target), findLast(nums, target)]