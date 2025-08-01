from collections import Counter

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        count = 0

        for num in freq:
            if num + k in freq:
                count += freq[num] * freq[num + k]
        
        return count
