class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        big_arr=[]
        for i in range(0,numRows):
            sub_arr=[0]*(i+1) #this will create a sub_arr having length equal to number of elements in each row
            sub_arr[0]=1 #1st element in a row will always be 1
            sub_arr[i]=1 #last element in a row will always be 1
            #j loop is only used from 3rd row onwards
            for j in range(1,len(sub_arr)-1): #for 1st and 2nd rows this loop will be skipped, bcoz for the 1st iteration range(1,0) will not get executed and similarly for 2nd iteration range(1,1) will not get executed
                sub_arr[j]=previous_arr[j]+previous_arr[j-1]
            big_arr.append(sub_arr)
            previous_arr=sub_arr
        return big_arr
