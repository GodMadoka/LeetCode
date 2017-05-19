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
        if len(prices) < 2: return 0
        dp = [0]
        minp = prices[0]
        for i in xrange(1,len(prices)):
               if minp > prices[i]: minp = prices[i]
               dp[i] = max(dp[i-1], prices[i] - minp)        
        return dp[len(prices) - 1]