class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map={}
        for x in nums:
            if x not in hash_map:
                hash_map.update({x:1})
            else:
                value=hash_map[x]+1
                hash_map.update({x:value})
        target=len(nums)/2
        for key in hash_map:
            if(hash_map[key]>target):
                return key