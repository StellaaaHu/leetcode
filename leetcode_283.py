#encoding:utf-8
#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#Note:
#You must do this in-place without making a copy of the array.
#Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = temp = 0
        while n < len(nums):
        	if nums[n] == 0:
        		temp += 1
        		nums.remove(nums[n])
        		n -= 1
        	n += 1
        while temp > 0:
        	nums.append(0)
        	temp -= 1