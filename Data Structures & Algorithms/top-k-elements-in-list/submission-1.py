from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        KFrequent=Counter(nums).most_common(k)
        
        for element,_ in KFrequent : 
            result.append(element)
        return(result)
