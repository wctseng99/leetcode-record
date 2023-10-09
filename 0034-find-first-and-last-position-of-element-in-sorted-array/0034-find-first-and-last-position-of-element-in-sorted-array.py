class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, is_search_left_side):
            left = 0
            target_index = -1
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    # mid = target
                    target_index = mid
                    if is_search_left_side:
                        # find the left most target
                        right = mid - 1
                    else:
                        left = mid + 1 
            return target_index
        return [binary_search(nums, target, True), binary_search(nums, target, False)]
                
