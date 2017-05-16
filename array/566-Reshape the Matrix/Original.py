# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def matrixReshape(nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0]) != r*c:
            return nums
        res = []
        for i in xrange(r):
            res.append([])
        col = 0
        for i in xrange(len(nums)):
            for j in xrange(len(nums[0])):
                res[col].append(nums[i][j]) 
                if (i*len(nums[0])+j+1)%c == 0:
                    col += 1
                
        return res

a = [[1,2],[3,4]]
print matrixReshape(a, 1, 4)