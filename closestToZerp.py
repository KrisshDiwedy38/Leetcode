def closesttozero(nums):
   min = nums[0]
   for num in nums:
      if num ==0:
         return num
      elif abs(num) < abs(min):
         min = num
      elif abs(num) == abs(min):
         if num > min:
            min = num
   return min

print(closesttozero([1,-1,4,56,8,-2,2]))
   