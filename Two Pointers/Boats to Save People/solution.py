class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        i, j = 0, n-1
        count = 0

        while i < j:
            if (weight := people[i] + people[j]) <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            count += 1
        
        if i == j:
            count += 1
        
        return count
    

# * Counting sort

from math import ceil
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people_freq = [0] * (limit + 1)
        for person in people:
            people_freq[person] += 1
        
        count = 0
        i, j = 0, limit
        while i < j:
            if people_freq[i] == 0:
                i += 1
                continue

            if people_freq[j] == 0:
                j -= 1
                continue
            
            if (i + j) > limit:
                count += people_freq[j]
                j -= 1
            elif people_freq[i] == people_freq[j]:
                count += people_freq[i]
                i += 1
                j -= 1
            elif people_freq[i] < people_freq[j]:
                count += people_freq[i]
                people_freq[j] -= people_freq[i]
                i += 1
            else:
                count += people_freq[j]
                people_freq[i] -= people_freq[j]
                j -= 1
        
        if i == j:
            if (2 * i) <= limit:
                count += ceil(people_freq[i] / 2)
            else:
                count += people_freq[j]
        
        return count