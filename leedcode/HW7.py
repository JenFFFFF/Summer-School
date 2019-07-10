# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:29:53 2019

@author: user
"""
#258. Add Digits

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #input: 1~9 -> only one digit
        #output: 1~9
        #input 10~.... -> internal add
        #output: 1,2,3,4,5,6,7,8,9,1(19),2(20),...,9,1,....
        
        #intput 38
        #(38-1) mod 9 = 37 mod 9 = 1 + 1 = 2
        
        if num<=0:
            return 0
        else:
            result=(num-1)%9+1
        return result