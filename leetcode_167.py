#encoding:utf-8
#Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#The function twoSum should return indices of the two numbers such that they add up to the target, 
#where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#You may assume that each input would have exactly one solution and you may not use the same element twice.

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = 0
        result_arr = []
        while count < len(numbers) -1 and numbers[count] <= target:
        	if numbers[count] == numbers[count + 1]:
        		if numbers[count] + numbers[count + 1] == target:
        			result_arr.append(count + 1)
        			result_arr.append(count + 2)
        			break
        		else:
        			count += 1
        	else:
        		for n in range(count + 1, len(numbers)):
        			if numbers[count] + numbers[n] == target:
        				result_arr.append(count + 1)
        				result_arr.append(n + 1)
        				break
        		count += 1
        return result_arr