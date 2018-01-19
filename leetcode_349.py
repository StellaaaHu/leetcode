#encoding:utf-8
#Given two arrays, write a function to compute their intersection.

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        n = 1
        while n < len(nums1):
        	if nums1[n] == nums1[n - 1]:
        		del nums1[n]
        		n -= 1
        	n += 1
        n = 1
        while n < len(nums2):
        	if nums2[n] == nums2[n - 1]:
        		del nums2[n]
        		n -= 1
        	n += 1
        m = 0
        result_arr = []
        while m < len(nums2):
        	if nums2[m] in nums1:
        		result_arr.append(nums2[m])
        	m += 1
        return result_arr