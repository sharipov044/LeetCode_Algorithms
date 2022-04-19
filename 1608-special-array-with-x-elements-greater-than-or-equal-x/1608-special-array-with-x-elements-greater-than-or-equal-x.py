class Solution:
    def specialArray(self, nums: List[int]) -> int:
         x = 0
        
         while x <= len(nums):
             count = 0
             for num in nums:
                 if num >= x:
                     count += 1

             if count == x:
                 return x
            
             x += 1
        
         return -1
        