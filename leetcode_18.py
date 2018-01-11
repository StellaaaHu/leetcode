#encoding:utf-8 
#Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
#Find all unique quadruplets in the array which gives the sum of target
#The solution set must not contain duplicate quadruplets.

#从一个有n个整数元素的数组中找出相加和为target的四项组合。（找出所有组合 & 不能是重复的）

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        s_arr = nums
        s_target = target
        q1_control = 0
        sum_temp = 0
        result_arr = temp_arr = []
        while q1_control <= len(s_arr) - 4:
        	sum_temp += s_arr[q1_control]
        	q2_control = q1_control + 1
        	while q2_control <= len(s_arr) - 3:
        		sum_temp += s_arr[q2_control]
        		q3_control = q2_control + 1
        		while q3_control <= len(s_arr) -2:
        			sum_temp += s_arr[q3_control]
        			q4_control = q3_control + 1
        			while q4_control <= len(s_arr) - 1:
        				sum_temp += s_arr[q4_control]
        				if sum_temp == s_target:
        					temp_arr = [s_arr[q1_control], s_arr[q2_control], s_arr[q3_control], s_arr[q4_control]]
        					result_arr.append(temp_arr)
        				sum_temp -= s_arr[q4_control]
        				q4_control += 1
        			sum_temp -= s_arr[q3_control]
        			q3_control += 1
        		sum_temp -= s_arr[q2_control]
        		q2_control += 1
        	sum_temp -= s_arr[q1_control]
        	q1_control += 1
        for n in range(0, len(result_arr)):
        	result_arr[n] = sorted(result_arr[n])
        filt = 0
        output_arr = []
        while filt <= len(result_arr) - 1:
        	if result_arr[filt] not in output_arr:
        		output_arr.append(result_arr[filt])
        	filt += 1
        return output_arr

