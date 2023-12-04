class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        for i in range(l):
            nums[i]=(nums[nums[i]] % l) * l + nums[i]
        for i in range(l):
            nums[i]=nums[i]//l
        return nums
        
