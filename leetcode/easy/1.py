class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            ans.append(sum)
        return ans

nums = [1,2,3,4]
a=Solution()
a.runningSum(nums)