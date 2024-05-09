class Solution:
    def solve(self, nums, k):
        n = len(nums)
        i = 0
        j = 0
        summation = 0
        ans = 0

        while j < n:
            summation += nums[j]
            while summation > k:
                summation -= nums[i]
                i += 1
            ans += j - i + 1
            j += 1
        
        return ans

    def countSubarray(self, N, A, L, R):
        return self.solve(A, R) - self.solve(A, L - 1)
