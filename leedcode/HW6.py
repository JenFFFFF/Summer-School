# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:29:53 2019

@author: user
"""
#326. Power of Three

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        elif n<=2:
            return False
        
        while n>3:
            if n%3==0:
                n/=3
            else:
                return False
            
        if n==3:
            return True
        else:
            return False