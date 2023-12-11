class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list=[]
        sum=0
        for i in nums:
            sum=sum+i
            new_list.append(sum)
        return new_list