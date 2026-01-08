class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l, r = 0, n - 1

        i = -1
        while l+1 < r:

            mid = l + (r - l) // 2
            mid_ele = mountainArr.get(mid)
            left_ele = mountainArr.get(l)
            right_ele = mountainArr.get(r)
            
            if left_ele < mid_ele and mid_ele > right_ele:
                i = mid

                if mid > 0:
                    prev_ele = mountainArr.get(mid-1)
                    if prev_ele < mid_ele:
                        l = mid
                    else:
                        r = mid

                else:
                    next_ele = mountainArr.get(mid+1)
                    if mid_ele > next_ele:
                        r = mid
                    else:
                        l = mid

            elif left_ele < mid_ele < right_ele:
                l = mid
            
            elif left_ele > mid_ele > right_ele:
                r = mid
            
            else:
                # print(left_ele, mid_ele, right_ele, i)
                l += 1
        

        l, r = 0, i
        while l <= r:
            mid = l + (r - l) // 2
            mid_ele = mountainArr.get(mid)
            if target == mid_ele:
                return mid
            elif target < mid_ele:
                r = mid - 1
            else:
                l = mid + 1
        
        l, r = i+1, n-1
        while l <= r:
            mid = l + (r - l) // 2
            mid_ele = mountainArr.get(mid)
            if target == mid_ele:
                return mid
            elif target > mid_ele:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1



class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l, r = 1, n - 2

        while l <= r:

            mid = l + (r - l) // 2
            mid_ele = mountainArr.get(mid)
            left_ele = mountainArr.get(mid - 1)
            right_ele = mountainArr.get(mid + 1)
            
            if left_ele < mid_ele < right_ele:
                l = mid + 1
            
            elif left_ele > mid_ele > right_ele:
                r = mid - 1
            
            else:
                break
        
        i = mid

        l, r = 0, i
        while l <= r:
            mid = l + (r - l) // 2
            mid_ele = mountainArr.get(mid)
            if target == mid_ele:
                return mid
            elif target < mid_ele:
                r = mid - 1
            else:
                l = mid + 1
        
        l, r = i+1, n-1
        while l <= r:
            mid = l + (r - l) // 2
            mid_ele = mountainArr.get(mid)
            if target == mid_ele:
                return mid
            elif target > mid_ele:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1



class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        cache = {}

        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]

        l, r = 1, n - 2
        while l <= r:
            mid = l + (r - l) // 2
            mid_ele = get(mid)
            left_ele = get(mid - 1)
            right_ele = get(mid + 1)
            
            if left_ele < mid_ele < right_ele:
                l = mid + 1
            
            elif left_ele > mid_ele > right_ele:
                r = mid - 1
            
            else:
                break
        
        i = mid

        l, r = 0, i
        while l <= r:
            mid = l + (r - l) // 2
            mid_ele = get(mid)
            if target == mid_ele:
                return mid
            elif target < mid_ele:
                r = mid - 1
            else:
                l = mid + 1
        
        l, r = i+1, n-1
        while l <= r:
            mid = l + (r - l) // 2
            mid_ele = get(mid)
            if target == mid_ele:
                return mid
            elif target > mid_ele:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
