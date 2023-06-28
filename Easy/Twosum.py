class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = [];
        Findex = 0;
   
        while (Findex <= len(nums)):
            Sindex = Findex + 1;
            while (Sindex < len(nums)):

                if (nums[Findex] + nums[Sindex] == target):
                    answer.append(Findex)
                    answer.append(Sindex)
                    return(answer)
                else:
                    Sindex = Sindex + 1;

            Findex = Findex +1;