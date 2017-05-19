# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:33:58 2017

@author: Ye WANG(ars_saki)
"""
'''
class Solution(object):
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
               for j in xrange(i+1,len(nums)):
                      if(nums[i]+nums[j]==target):
                             return i,j
    '''                  
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in xrange(len(nums)):
               if target - nums[i] in dic:
                      return i,dic[target-nums[i]]
               else:
                      dic[nums[i]] = i