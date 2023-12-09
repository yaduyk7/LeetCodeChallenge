class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pt1=0
        pt2=len(nums)-1
        while(pt1<=pt2):
            if(nums[pt1]==0):
                a=nums.pop(pt1)
                nums.append(a)
                pt2-=1
            else:
                pt1+=1
