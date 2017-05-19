# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:58:50 2017

@author: Ye WANG(ars_saki)
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) < 2): return len(nums)
        i = 1
        j = 1
        while i < len(nums):
               if(nums[i]!=nums[j-1]): 
                      nums[j] = nums[i]
                      j += 1
               i += 1
        return j            
 
