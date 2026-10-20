class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique = Counter(nums)
        res = []

        for num, freq in unique.most_common(k):
            res.append(num)

        return res