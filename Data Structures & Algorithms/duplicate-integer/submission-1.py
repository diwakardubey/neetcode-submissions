from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = Counter(nums)
        for _,v in num_count.items() :
            if v > 1 : 
                return True
        return False
        