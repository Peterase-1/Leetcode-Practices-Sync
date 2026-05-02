class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array for optimization
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_len = m + n
        half = total_len // 2
        
        # Binary search on the smaller array
        left, right = 0, m
        
        while left <= right:
            # Partition nums1
            i = (left + right) // 2  # mid of nums1
            j = half - i             # corresponding partition in nums2
            
            # Get the four boundary elements
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            # Check if we found the correct partition
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Correct partition found
                if total_len % 2 == 1:
                    # Odd total length
                    return min(nums1_right_min, nums2_right_min)
                else:
                    # Even total length
                    left_max = max(nums1_left_max, nums2_left_max)
                    right_min = min(nums1_right_min, nums2_right_min)
                    return (left_max + right_min) / 2.0
            elif nums1_left_max > nums2_right_min:
                # nums1's left half is too big, move left
                right = i - 1
            else:
                # nums1's left half is too small, move right
                left = i + 1
        
        return 0.0  # Should never reach here for valid input