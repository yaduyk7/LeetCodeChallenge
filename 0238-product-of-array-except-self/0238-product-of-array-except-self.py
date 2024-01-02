class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length=len(nums)
        output=[1]*length
        l_prod=1
        r_prod=1
        for i in range(length-1):
            l_prod=l_prod*nums[i]
            output[i+1]=l_prod
        for j in range(length-1,0,-1):
            r_prod=r_prod*nums[j]
            output[j-1]*=r_prod
        return output