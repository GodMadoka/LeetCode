# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:10:59 2017

@author: Ye WANG(ars_saki)
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums,k):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for i in xrange(len(nums)):
        	if nums[i] in dic and i - dic[nums[i]] <= k: return True
        	else: dic[nums[i]] = i
        return False
                      
        
