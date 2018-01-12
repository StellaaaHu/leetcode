#encoding:utf-8
#Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#Find all the elements of [1, n] inclusive that do not appear in this array.
#Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        original_arr = sorted(nums)
        new_arr = list(set(original_arr))
        total = len(original_arr)
        m = 0
        temp = 1
        output_arr = []
        while m < total and temp <= total:
        	if m < len(new_arr):
        		if new_arr[m] != temp:
        			output_arr.append(temp)
        			m -= 1
        	else:
        		output_arr.append(temp)
        	temp += 1
        	m += 1
        return output_arr