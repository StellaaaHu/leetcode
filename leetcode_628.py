#encoding:utf-8
#Given an integer array, find three numbers whose product is maximum and output the maximum product.

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        left_product = nums[0] * nums[1]
        right_product = nums[-1] * nums[-2]
        if left_product * nums[-1] > right_product * nums[-3]:
        	result_product = left_product * nums[-1]
        else:
        	result_product = right_product * nums[-3]
        return result_product