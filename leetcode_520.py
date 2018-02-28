#encoding:utf-8
#Given a word, you need to judge whether the usage of capitals in it is right or not.
#We define the usage of capitals in a word to be right when one of the following cases holds:
#All letters in this word are capitals, like "USA".#All letters in this word are not capitals, like "leetcode".
#Only the first letter in this word is capital if it has more than one letter, like "Google".
#Otherwise, we define that this word doesn't use capitals in a right way.

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        temp = True
        if len(word) > 1:
        	if 'A' <= word[0] <= 'Z':
        		if 'A' <= word[1] <= 'Z':
        			for n in range(2, len(word)):
        				if 'a' <= word[n] <= 'z':
        					temp = False
        					break
        				else:
        					temp = True
        		else:
        			for n in range(2, len(word)):
        				if 'A' <= word[n] <= 'Z':
        					temp = False
        					break
        				else:
        					temp = True
        	else:
        		for n in range(1, len(word)):
        			if 'A' <= word[n] <= 'Z':
        				temp = False
        				break
        			else:
        				temp = True
        return temp