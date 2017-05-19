# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:26:02 2017

@author: Ye WANG(ars_saki)
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        cur = len(digits) - 1
        digits[cur] += 1
        while(digits[cur] == 10):
               digits[cur] = 0               
               if(cur == 0):
                      digits.insert(0,1)
                      break
               else:
                      digits[cur-1] += 1
                      cur = cur - 1
        return digits
               