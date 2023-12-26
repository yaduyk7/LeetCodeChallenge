class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        output=[]
        intervals.sort()
        for start, end in intervals:
            if(len(output)==0):
                output.append([start,end])
            else:
                if(start <= output[-1][-1]):
                    output[-1][-1]=max(output[-1][-1],end)
                else:
                    output.append([start,end])
        return output