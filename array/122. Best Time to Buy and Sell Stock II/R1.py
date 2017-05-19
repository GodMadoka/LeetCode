# -*- coding: utf-8 -*-
"""
Created on Thu May 18 20:40:58 2017

@author: Ye WANG(ars_saki)
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2: return 0
        buyprice = prices[0]
        cntprice = prices[0]
        res = 0
        for i in xrange(1,len(prices)):
               if prices[i] > cntprice:
                      cntprice = prices[i]
               else:
                      res += cntprice - buyprice
                      cntprice = prices[i]
                      buyprice = prices[i]
        res += cntprice - buyprice
        return res

'''
Basically, if tomorrow's price is higher than today's, we buy it today and sell tomorrow. 
Otherwise, we don't. 
Notice that we can sell and buy it in one day.
''' 
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i]-prices[i-1],0) for i in xrange(1,len(prices)))