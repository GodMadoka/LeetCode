# -*- coding: utf-8 -*-
"""
Created on Wed May 17 18:20:24 2017

@author: Ye WANG(ars_saki)
"""
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i < j:
               if(nums[i]==val):
                      while(j >= 0 and nums[j]==val): j = j - 1
                      if(j > i): 
                             nums[i] = nums[j]
                             j -= 1
               i += 1
        while(j >= 0 and nums[j]==val): j = j - 1      
        return j + 1
'''

class Solution(object):
       def removeElement(self, nums, val):
           """
           :type nums: List[int]
           :type val: int
           :rtype: int
           """
           index = 0
           for i in xrange(len(nums)):
                  if(nums[i]!=val):
                         nums[index] = nums[i]
                         index += 1
           return index
if __name__ == "__main__":
       a = Solution()
       print a.removeElement([3,2,2,3],2)