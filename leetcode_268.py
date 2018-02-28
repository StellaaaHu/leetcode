#encoding:utf-8
#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        nums.append(' ')
        for n in range(0, len(nums)):
        	if nums[n] != n:
        		return n