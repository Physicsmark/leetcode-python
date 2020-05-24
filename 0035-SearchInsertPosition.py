class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Case 1: insert at the head
        if len(nums) == 0 or target <= nums[0]:
            return 0
        # Case 2: insert at the tail
        if target > nums[-1]:
            return len(nums)
        # Case 3: otherwise
        i = 1
        while i < len(nums):
            if target > nums[i]:
                i += 1
                continue
            return i
