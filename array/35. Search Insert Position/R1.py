# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:43:56 2017

@author: Ye WANG(ars_saki)
"""

class Solution(object):       
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0; h = len(nums) - 1
        while(l<=h):
               m = l + (h - l)/2
               if(nums[m] < target): l = m + 1
               else: h = m - 1
        return l



