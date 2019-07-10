# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:29:53 2019

@author: user
"""
#28. Implement strStr()

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        