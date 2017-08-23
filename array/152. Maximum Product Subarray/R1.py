# -*- coding: utf-8 -*-
"""
Created on Thu May 18 19:27:46 2017

@author: Ye WANG(ars_saki)
"""

'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxpos = 0
        maxneg = 0
        res = float("-inf")
        if len(nums) < 2: return nums[0]
        for i in nums:               
               if i > 0:                      
                      maxpos *= i
                      maxneg *= i
                      if maxpos == 0: maxpos = i
               elif i < 0:
                      cntmaxpos = maxneg * i
                      cntmaxneg = maxpos * i
                      maxneg = cntmaxneg
                      maxpos = cntmaxpos
                      if maxneg == 0: maxneg = i
               else:
                      maxpos = 0
                      maxneg = 0
               res = max(res,maxpos,maxneg)
        return res
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        premax = nums[0]
        premin = nums[0]
        res = nums[0]
        for i in xrange(1,len(nums)):
               cntmax = max(premax*nums[i],premin*nums[i],nums[i])
               cntmin = min(premax*nums[i],premin*nums[i],nums[i])
               res = max(res,cntmax)
               premax = cntmax
               premin = cntmin
        return res

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        maxpos = 1
        maxneg = 1
        for i in nums:
        	cntpos = max(maxpos*i,maxneg*i,i)
        	cntneg = min(maxpos*i,maxneg*i,i)
        	maxpos = cntpos
        	maxneg = cntneg
        	res = max(res,maxpos,i)
        return res

