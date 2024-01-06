class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        l=0
        r=1
        flag=0
        while(r<len(nums)):
            if(nums[l]==nums[r]):
                flag=1
                return True
            l+=1
            r+=1
        if(flag==0):
            return False