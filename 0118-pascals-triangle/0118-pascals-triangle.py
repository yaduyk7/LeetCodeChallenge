class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        big_arr=[]
        for i in range(0,numRows):
            sub_arr=[0]*(i+1) 
            sub_arr[0]=1
            sub_arr[i]=1
            for j in range(1,len(sub_arr)-1):
                sub_arr[j]=previous_arr[j]+previous_arr[j-1]
            big_arr.append(sub_arr)
            previous_arr=sub_arr
        return big_arr