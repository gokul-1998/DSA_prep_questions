class Solution:
    # first set the left and right initializations
    #  do a while loop and set the mid value
    # check for target and mid equality
    # if nums[left]<=nums[mid] check if nums[left]<=target<=nums[mid] 
    # else check if nums[mid]<=target<=nums[right]
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1