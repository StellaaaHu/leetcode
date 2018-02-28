#encoding:utf-8
#Given an array and a value, remove all instances of that value in-place and return the new length.
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = 0
        while n < len(nums):
        	if nums[n] == val:
        		nums.remove(nums[n])
        		n -= 1
        	n += 1
        return len(nums)