class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        target_triplet = [0, 0, 0]

        for triplet in triplets:
            if all(triplet[i] <= target[i] for i in range(3)):
                target_triplet = [
                    max(triplet[0], target_triplet[0]),
                    max(triplet[1], target_triplet[1]),
                    max(triplet[2], target_triplet[2])
                ]
                if target_triplet == target:
                    return True
        
        return False
        
