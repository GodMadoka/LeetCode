# -*- coding: utf-8 -*-
"""
Created on Wed May 17 19:52:34 2017

@author: Ye WANG(ars_saki)

For each number i in nums,
we mark the number that i points as negative.
Then we filter the list, get all the indexes
who points to a positive number.
Since those indexes are not visited.
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
               index = abs(i) - 1
               nums[index] = -abs(nums[index])
        return [v + 1 for v in xrange(len(nums)) if nums[v] > 0]