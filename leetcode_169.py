#encoding:utf-8
#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#You may assume that the array is non-empty and the majority element always exist in the array.

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        obj = {}
        for n in range(0, len(nums)):
        	obj[nums[n]] = obj[nums[n]] + 1 if nums[n] in obj else 1
        	if obj[nums[n]] > len(nums) / 2:
        		return nums[n]
        		break