class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums)
        elif length == 0:
            return 0

        max_money = [0] * len(nums)
        max_money[0] = nums[0]
        max_money[1] = max(nums[0], nums[1])
        i = 2
        while i < length:
            max_money[i] = max(max_money[i-2] + nums[i], max_money[i-1])
            i += 1
        
        return max_money[length - 1]
