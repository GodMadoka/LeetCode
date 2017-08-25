class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cntmax = float('-inf')
        l = -1; r = -2
        for i in xrange(len(nums)):
            if cntmax <= nums[i]:
                cntmax = nums[i]
            else:
                r = i
                if l == -1: l = i - 1
                while l > 0 and nums[l - 1] > nums[i]: l -= 1
        return r - l + 1
