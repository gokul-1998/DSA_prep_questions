class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1

        while left<=right:
            mid=(left+right)//2
        
            if nums[mid]==target:
                return mid

            if nums[left]<=nums[mid]:
                # if nums[left]<=target<=nums[right]: made a mistake here
                if nums[left]<=target<=nums[mid]:
                    # right=nums[mid-1] another mistake
                    right=mid-1
                else:
                    # left = nums[mid+1]
                    left=mid+1
            else:
                if nums[right]<=nums[mid]:
                    if nums[mid]<=target<=nums[right]:
                        # left=nums[mid+1]
                        left=mid+1
                    else:
                        # right=nums[mid-1]
                        right=mid-1
        
        return -1