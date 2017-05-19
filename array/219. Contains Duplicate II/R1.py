# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:10:59 2017

@author: Ye WANG(ars_saki)
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in xrange(len(nums)):
               if nums[i] not in dic():
                      dic[nums[i]] = i
               else:
                      if abs(dic[nums[i]] - i) <= k:
                             return True
                      dic[nums[i]] = i
        return False
                      
        