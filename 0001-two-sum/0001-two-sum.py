class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map={} #declaring a dictionary named 'hash_map'
        new_list=[]
        for index, value in enumerate(nums):
            diff=target-value
            if diff in hash_map:
                new_list.append(index)
                new_list.append(hash_map[diff])
                break
            else:
                hash_map.update({value:index})
        return new_list

