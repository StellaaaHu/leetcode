#encoding:utf-8

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        obj = {}
        num_arr = []
        for i in range(0, len(nums)):
        	obj[nums[i]] = obj[nums[i]] + 1 if nums[i] in obj else 1
        max_num = max(obj.values())
        if max_num == 1:
        	return 1
        else:
        	for key,value in obj.items():
        		if value == max_num:
        			num_arr.append(key)
        	result = 50000
        	for m in range(0, len(num_arr)):
        		index_arr = []
        		for n in range(0, len(nums)):
        			if nums[n] == num_arr[m]:
        				index_arr.append(n)
        			n += 1
        		temp = max(index_arr) - min(index_arr) + 1
        		if temp < result:
        			result = temp
        		m += 1
        	return result