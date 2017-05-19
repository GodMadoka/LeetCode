# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:20:23 2017

@author: Ye WANG(ars_saki)
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        maxlen = 0
        for i in xrange(len(nums)):
               if(nums[i] == 1):
                      cnt += 1
               else:
                      maxlen = max([cnt,maxlen])
                      cnt = 0
        return max([cnt,maxlen])
   