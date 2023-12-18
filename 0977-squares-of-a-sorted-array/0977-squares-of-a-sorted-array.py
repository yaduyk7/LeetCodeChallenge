class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pt1=0 #left pointer
        pt2=len(nums)-1 #right pointer
        pt3=len(nums)-1 #pointer to track new list
        arr=[0]*len(nums) #creating a new list with same size that of nums 
        while(pt3>=0):
            if(nums[pt1]**2 >= nums[pt2]**2): #comparing squares of first and last elements
                arr[pt3]=nums[pt1]**2
                pt1+=1
            else:
                arr[pt3]=nums[pt2]**2
                pt2-=1
            pt3-=1
        return arr

        