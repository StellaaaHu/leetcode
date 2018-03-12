#encoding:utf-8
#Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
#Find all unique triplets in the array which gives the sum of zero.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result_arr = []
        nums = sorted(nums)
        for a in range(len(nums) - 2):
        	left = a + 1
        	right = len(nums) - 1
        	while left < right:
        		sum_up = nums[a] + nums[left] + nums[right]
        		if sum_up == 0 and [nums[a], nums[left], nums[right]] not in result_arr:
        			result_arr.append([nums[a], nums[left], nums[right]])
        			left += 1
        			right -= 1
        		elif sum_up < 0:
        			left += 1
        		else:
        			right -= 1
        return result_arr