
# Problem: House Robber
# LeetCode: https://leetcode.com/problems/house-robber/
# Approach: Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
