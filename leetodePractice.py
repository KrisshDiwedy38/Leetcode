def twoSum( nums, target):
   visited = []
   for i in range(0,nums):
      if target - nums[i] in visited:
         
      else:
         visited.append(i)
      
print(twoSum([2,7,11,15],9))