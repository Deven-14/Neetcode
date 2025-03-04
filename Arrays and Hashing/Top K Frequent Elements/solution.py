from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [key for key, _ in Counter(nums).most_common(k)]
    


from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for i in range(len(nums)+1)] # bucket sort based on freq, there can only be [1, len(nums)] freq
        counts = Counter(nums)

        for num, freq in counts.items():
            freqs[freq].append(num)
        
        topk = []
        for i in range(len(freqs)-1, 0, -1):
            for num in freqs[i]:
                topk.append(num)
                if len(topk) == k:
                    return topk

# return [key for key, _ in Counter(nums).most_common(k)]