# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:52:31 2017

@author: Ye WANG(ars_saki)
"""
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float("-inf")
        mxsum = 0
        for i in xrange(len(nums)):
             mxsum += nums[i]
             if mxsum < 0 : mxsum = 0
             if mxsum > res: res = mxsum
        if res <= 0:
               res = float("-inf")
               for i in nums:
                      res = max(res,i)
        return res
'''

class Solution(object):
   def maxSubArray(self,nums):
       """
       :type nums: List[int]
       :rtype: int
       """
       res = float("-inf")
       dp = 0
       for i in xrange(len(nums)):
              if dp < 0:
                     dp = nums[i]
              else:
                     dp += nums[i]
              if dp > res:
                     res = dp
       return res
'''
the idea is: for each sub array we calculate 4 values in O(1) time 
 based on the return values of its two halves. The meaning of the values:

l: the sum of the sub array with largest sum starting from the first element
m: the sum of the sub array with largest sum
r: the sum of the sub array with largest sum ending at the last element
s: the sum of the whole array
'''
class SolutionByDivideAndConquer(object):
   def maxSubArray(self,nums):
       """
       :type nums: List[int]
       :rtype: int
       """
       return self.maxSum(nums,0,len(nums)-1)[1]
   def maxSum(self,nums,a,b):# l m r s
          if b - a < 1: return nums[a],nums[a],nums[a],nums[a]
          m = a + (b - a) / 2          
          v1 = self.maxSum(nums,a,m)
          v2 = self.maxSum(nums,m+1,b)
          l = max(v1[0],v1[3]+v2[0])
          m = max(v1[1],v2[1],v1[2]+v2[0])
          r = max(v2[2],v1[2]+v2[3])
          s = v1[3]+v2[3]
          return l,m,r,s
                 
       