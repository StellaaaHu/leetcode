#encoding:utf-8

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        output_arr = []
        count = len(list1) + len(list2)
        i = 0
        while i < len(list1):
        	if list1[i] in list2:
        		j = list2.index(list1[i])
        		if i + j < count:
        			count = i + j
        			output_arr = []
        			output_arr.append(list1[i])
        		elif i + j == count:
        			output_arr.append(list1[i])
        	i += 1
        return output_arr