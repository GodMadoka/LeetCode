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
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
        	if i in dic:
        		dic[i] += 1
        	else:
        		dic[i] = 1
        res = 0
        flag = True
        for i in xrange(-10000,10001):
        	if i in dic:
        		for j in xrange(dic[i]):
        			if flag:
        				res += i
        			flag = not flag
        return res

a = [1,4,3,2]
print arrayPairSum(a)
