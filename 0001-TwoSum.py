class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_maps = {}
        for i, n in enumerate(nums):
            if target - n in num_maps:
                return [num_maps[target - n], i]
            num_maps[n] = i
        return []
