#encoding:utf-8
#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        result = False
        for n in range(0, len(nums) - 1):
        	if nums[n + 1] == nums[n]:
        		result = True
        		break
        return result