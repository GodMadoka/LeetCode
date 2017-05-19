# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:40:46 2017

@author: Ye WANG(ars_saki)
"""
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt = nums.count(0)
        for i in xrange(cnt):
               nums.remove(0)
               nums.append(0)
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cur = 0
        for i in xrange(len(nums)):
               if(nums[i] != 0):
                      nums[cur],nums[i] = nums[i],nums[cur]
                      cur += 1