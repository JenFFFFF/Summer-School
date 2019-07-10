# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:29:53 2019

@author: user
"""
#66. Plus One

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):  #數列倒序
            if digits[i]==9:  #9進位為0
                digits[i]=0
            else:
                digits[i]+=1  
                return digits
        digits[0]=1  #0進位為1
        digits.append(0)  #尾數加一個0
            #input 999
            #output 000 => 100 => 1000
        return digits