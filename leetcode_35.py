#encoding:utf-8
#Given a sorted array and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = 0
        if nums[0] > target:
        	index = 0
        elif nums[-1] < target:
        	index = len(nums)
        else:
        	for n in range(0, len(nums)):
        		if nums[n] >= target:
        			index = n
        			break
        		n += 1
        return index