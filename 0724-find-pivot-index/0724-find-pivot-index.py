class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_left=0
        sum_right=0
        sum1=0
        flag=0
        for j in range(1,len(nums)):
            sum_left=sum_left+nums[j]
        for j in range(len(nums)-1):
            sum_right=sum_right+nums[j]
        if(sum_left==0):
            return 0
        tot_sum=sum(nums)
        L_sum=0
        R_sum=0
        for i in range(1,len(nums)):
            L_sum=L_sum+nums[i-1]
            R_sum=tot_sum-(nums[i]+L_sum)
            if(L_sum==R_sum):
                flag=1
                return i

        if(sum_right==0):
            return len(nums)-1

        if(flag==0):
            return -1