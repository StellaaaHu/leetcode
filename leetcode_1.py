#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#规定一个目标数值，找出一个int型数组中相加等于目标数值的两个元素的下标（可以假设数组中不存在重复元素且一个数组中都必有且只有一组目标值）

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i < (len(nums) - 1):
        	control = target - nums[i]
        	for j in range(i+1, len(nums)):
        		if nums[j] == control:
        			return i, j
        			break
        	i += 1

