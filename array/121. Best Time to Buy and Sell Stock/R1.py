# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:09:36 2017

@author: Ye WANG(ars_saki)
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxp = 0
        minp = float('inf')
        for p in prices:
        	if p < minp:
        		minp = p
        	if p - minp > maxp:
        		maxp = p - minp
        return maxp
