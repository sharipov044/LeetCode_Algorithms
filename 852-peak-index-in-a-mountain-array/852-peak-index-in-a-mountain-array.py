class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if not arr:
            return -1
        
        start = 0
        end = len(arr) - 1
        
        while start - 1 < end:
            mid = start + (end - start) // 2
            
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                start = mid
            else:
                end = mid
            
        if arr[end] > arr[start]:
            return end
        else:
            return start
        
        return -1
    