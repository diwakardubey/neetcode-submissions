from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : 
            return 0
        nums = list(set(nums) )
        nums_count = Counter(nums)
        print(nums_count)
        max_result = 0

        for num in nums : 
            if num -1 in nums_count.keys() : 
                continue 
            start_element = num 
            count = 1

            while start_element +1 in nums_count.keys() : 
                count += 1 
                start_element +=1 
            max_result = max(max_result,count)

        return max_result


        

        