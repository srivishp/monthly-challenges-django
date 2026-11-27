class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        final =[]
        i = 0
        j = 1
        while i < len(nums):
            while j < len(nums):
                if target == nums[i] + nums[j]:
                    final = [i,j]
                    return final
                else:
                    j += 1
            i += 1
            j = i + 1
        
