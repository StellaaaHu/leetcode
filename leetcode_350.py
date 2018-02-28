#encoding:utf-8
#Given two arrays, write a function to compute their intersection.
#Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = 0
        result_arr = []
        while n < len(nums2):
        	temp = nums2[n]
        	if temp in nums1:
        		result_arr.append(temp)
        		nums1.remove(temp)
        	n += 1
        return result_arr