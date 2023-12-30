class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[]
        nums.sort()
        for i in range(0,len(nums)-2):
            a=nums[i]
            left=i+1
            right=len(nums)-1
            target=-a
            while(right>left):
                if(nums[left]+nums[right] > target):
                    right-=1
                elif(nums[left]+nums[right] < target):
                    left+=1
                else:
                    arr=[]
                    arr.append(a)
                    arr.append(nums[left])
                    arr.append(nums[right])
                    if(arr not in output):
                        output.append(arr)
                    left+=1
                    right-=1
        return output
