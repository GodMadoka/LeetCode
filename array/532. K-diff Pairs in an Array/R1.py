# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:18:37 2017

@author: Ye WANG(ars_saki)
"""

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        res = 0
        for i in nums:
               if dic.has_key(i):
                      dic[i] += 1
               else:
                      dic[i] = 1
        if k<0: return 0               
        if k==0:
               for i in dic.keys():
                      if dic[i] > 1:
                             res += 1
               return res
       
        for i in dic.keys():
               if dic.has_key(i+k):
                      res += 1
        return res
 
