from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(is_left: bool):
            low, high = 0, len(nums) - 1
            bound = -1
            
            while low <= high:
                mid = (low + high) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if is_left:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return bound
        
        return [find(True), find(False)]
