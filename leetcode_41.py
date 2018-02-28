#encoding:utf-8
#Given an unsorted integer array, find the first missing positive integer.
#For example,
#Given [1,2,0] return 3, and [3,4,-1,1] return 2.
#Your algorithm should run in O(n) time and uses constant space.

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        n = result = 0
        if len(nums) == 0 or nums[-1] <= 0:
        	result = 1
        else:
        	while n < len(nums):
        		if nums[n] <= 0:
        			del nums[n]
        			n -= 1
        		else:
        			if nums[n] != n + 1:
        				result = n + 1
        				break
        		n += 1
        if result == 0:
        	result = nums[-1] + 1
        return result