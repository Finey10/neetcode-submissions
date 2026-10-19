from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for freq in counts.values():
            if freq > 1:
                return True      
        return False