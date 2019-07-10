# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:29:53 2019

@author: user
"""
#412. Fizz Buzz

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 != 0:  #3的倍數
                result.append('Fizz')
            elif i % 3 != 0 and i % 5 == 0:  #5的倍數
                result.append('Buzz')
            elif i % 3 == 0 and i % 5 == 0:  #3和5的倍數
                result.append('FizzBuzz')
            else:
                result.append(str(i))  #都不是
        return result