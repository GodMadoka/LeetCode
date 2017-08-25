class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in xrange(len(nums)):
        	idx = abs(nums[i]) - 1
        	if nums[idx] < 0:
        		res.append(idx + 1)
        	else:
        		nums[idx] = -nums[idx]
        return res
s = Solution()
nums = [4,3,2,7,8,2,3,1]
print s.findDuplicates(nums)
