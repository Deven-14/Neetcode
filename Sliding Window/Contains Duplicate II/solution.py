class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k += 1 # coz of 0 index
        if len(nums) < k:
            return len(nums) != len(set(nums))

        window_set = set(nums[:k])
        if len(window_set) < k:
            return True
        
        for i in range(k, len(nums)):
            window_set.remove(nums[i-k])
            if nums[i] in window_set:
                return True
            window_set.add(nums[i])
        
        return False