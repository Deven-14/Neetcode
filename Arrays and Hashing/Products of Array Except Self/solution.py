class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mul = 1
        pre = [ 
            (mul := mul * num)
            for num in nums
        ] # prefix
        mul = 1
        pre_rev = [0] * n # suffix
        for i in range(n-1, -1, -1):
            mul *= nums[i]
            pre_rev[i] = mul

        products = [pre_rev[1]]
        for i in range(1, n - 1):
            products.append(pre[i-1] * pre_rev[i+1])
        products.append(pre[-2])

        return products