#encoding:utf-8
#Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, 
#find the smallest element in the list that is larger than the given target.
#Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'

class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letters.append(target)
        letters = sorted(letters)
        if letters[-1] != target:
        	n = 0
        	while n < len(letters):
        		if letters[n] == target:
        			result_str = letters[n + 1]
        		n += 1
        else:
        	result_str = letters[0]
        return result_str