# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.
# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Solution
class Solution:
    def runningSum(self, nums):
        # Initialize the running sum to the first element
        running_sum = nums[0]

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Update the current element with the running sum
            nums[i] += running_sum

            # Update the running sum for the next iteration
            running_sum = nums[i]

        return nums
