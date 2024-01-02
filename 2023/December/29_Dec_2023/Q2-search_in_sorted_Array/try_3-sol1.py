class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set left and right initializations
        left,right=0,len(nums)-1

        # set the while loop
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid

        # if nums[left]<=nums[mid]:

            if nums[left]<=nums[mid]:
                if nums[left]<=target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                # since left is greater in value than mid
                if nums[mid]<=target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1

        return -1