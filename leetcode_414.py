#encoding:utf-8 
#Given a non-empty array of integers, return the third maximum number in this array. 
#If it does not exist, return the maximum number. The time complexity must be in O(n).

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = sorted(nums, reverse = True)
        if len(arr) > 1:
            n = control_temp = 1
            while n < len(arr) and control_temp <= 2:
            	if arr[n] != arr[n - 1]:
            		output = arr[n]
            		control_temp += 1
            	n += 1
            if control_temp <= 2:
            	output = arr[0]
        else:
        	output = arr[0]
        return output