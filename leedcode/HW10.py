# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:29:53 2019

@author: user
"""
#136. Single Number

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections  #集合
        cnt = collections.Counter(nums)  #計數
        cnt = dict(cnt)  #字典
        num = [x for x, y in cnt.items() if y == 1]
        return num[0]