#encoding:utf-8
#Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] 
#and the absolute difference between i and j is at most k.

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sorted_nums = sorted(nums)
        index_arr = []
        result = False
        for n in range(0, len(sorted_nums) - 1):
        	if sorted_nums[n + 1] == sorted_nums[n]:
        		equal_element = sorted_nums[n]
        		for m in range(0, len(nums)):
        			if nums[m] == equal_element:
        				index_arr.append(m)
        		for i in range(0, len(index_arr) - 1):
        			if index_arr[i + 1] - index_arr[i] <= k:
        				result = True
        				break
        		index_arr = []
        return result