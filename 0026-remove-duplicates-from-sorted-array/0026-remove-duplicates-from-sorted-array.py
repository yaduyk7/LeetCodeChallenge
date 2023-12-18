class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pt1=0
        pt2=1
        while(pt2<len(nums)):
            if (nums[pt1]!=nums[pt2]):
                pt1+=1
                nums[pt1],nums[pt2]=nums[pt2],nums[pt1]
            pt2+=1
        k=pt1+1 #pt1 will stop at last unique element. So number of unique elements will be pt1+1 bcoz pt1 starts from 0
        return k