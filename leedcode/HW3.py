# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:29:53 2019

@author: user
"""
#374. Guess Number Higher or Lower

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        #設區間
        left=1
        right=n
        
        while left<=right:
            mid=(left+right)/2
            ret=guess(mid)  #判斷有沒有猜中
            
            if ret==0:
                return mid
            elif ret==-1:
                right=mid-1
            else:
                left=mid+1