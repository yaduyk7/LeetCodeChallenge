class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag=0
        dict={}
        for num in nums:
            if num not in dict:
                dict.update({num:1})
            else:
                dict.update({num:dict[num]+1})
        for key in dict:
            if(dict[key]!=1):
                flag=1
        if(flag==1):
            return True
        else:
            return False