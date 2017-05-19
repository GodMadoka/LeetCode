# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:59:16 2017

@author: Ye WANG(ars_saki)
"""

def arrayPairSum(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in xrange(0,len(nums),2):
               res += nums[i]
        return res

a = [1,4,3,2]
print arrayPairSum(a)