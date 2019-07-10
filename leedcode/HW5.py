# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:29:53 2019

@author: user
"""
#53. Maximum Subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums)<0:  
            #看是不是所有的數都小於0,如果數裡面最大的小於0,就直接回傳
            return max(nums)  
        
        local_max,global_max=0,0
        for num in nums:
            local_max=max(0,local_max+num)  #兩者中找最大的
            global_max=max(global_max,local_max)  #兩者中找最大的
        return global_max