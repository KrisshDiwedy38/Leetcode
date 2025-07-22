def shift_k_places(nums,k):
   start = nums[-k:]
   limit = len(nums) - k - 1
   for i in range(limit,-1,-1):
      nums[i+k] = nums[i]

   nums[:k] = start
  

nums = [1,2,3,4,5,6,7] 
print(shift_k_places(nums,3))
print(nums)
