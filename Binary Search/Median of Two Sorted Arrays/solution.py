class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        half = n // 2

        l, r = 0, len(nums1) - 1
        while True:
            # nums1
            mid1 = (l + r) // 2
            left1 = nums1[mid1] if mid1 >= 0 else float("-inf")
            right1 = nums1[mid1 + 1] if (mid1 + 1) < len(nums1) else float("inf")

            other_half_of_partition = half - (mid1 + 1) # mid1+1 coz mid1 is idx,

            # nums2
            mid2 = other_half_of_partition - 1 # -1 coz we need idx
            left2 = nums2[mid2] if mid2 >= 0 else float("-inf")
            right2 = nums2[mid2 + 1] if (mid2 + 1) < len(nums2) else float("inf")

            print(left1, left2, right1, right2)
            if left1 <= right2 and left2 <= right1:
                if n % 2 == 1:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2)) / 2
            
            elif left1 > right2:
                r = mid1 - 1
            
            else:
                l = mid1 + 1

# ! come back to this later