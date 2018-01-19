#encoding:utf-8
#Given a List of words, 
#return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1 = ['q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P']
        row_2 = ['a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L']
        row_3 = ['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
        result_arr = []
        for n in range(0, len(words)):
        	temp = words[n]
        	if words[n][0] in row_1:
        		for m in range(1, len(words[n])):
        			if words[n][m] not in row_1:
        				temp = ''
        				break
        	if words[n][0] in row_2:
        		for m in range(1, len(words[n])):
        			if words[n][m] not in row_2:
        				temp = ''
        				break
        	if words[n][0] in row_3:
        		for m in range(1, len(words[n])):
        			if words[n][m] not in row_3:
        				temp = ''
        				break
        	if temp != '':
        		result_arr.append(temp)
        return result_arr