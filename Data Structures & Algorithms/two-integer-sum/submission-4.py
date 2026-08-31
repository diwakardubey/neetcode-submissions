class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums_dict = {}
        if n == 2 and sum(nums) == target:
            return[0,1]

        for i in range(len(nums)) : 
            diff = target - nums[i] 
            if diff in nums_dict : 
                if i < nums_dict[diff] : 
                    return [i, nums_dict[diff]]
                else : 
                    return [nums_dict[diff],i]
            nums_dict[nums[i]] = i


        



        