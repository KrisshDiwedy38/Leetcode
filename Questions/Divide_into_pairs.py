def dividing(nums):
   if len(nums) % 2 != 0:
      return False
   
   storage = {}
   for num in nums:
      if num in storage:
         storage[num] += 1
      else:
         storage[num] = 1
   for value in storage.values():
      if value % 2 != 0:
         return False
   return True


def dividing_two(nums):
   if len(nums) % 2 != 0:
      return False
   
   nums.sort()
   for i in range(0,len(nums)+1, 2):
      if nums[i] != nums[i+1]:
         return False
   return True



print(dividing([3,2,3,4,2,4]))
print(dividing_two([18,19,5,5,18,19,5,6,12,19,13,4,16,11,4,16,10,8,12,8,2,1,8,17,4,18,3,5,16,2,16,12,17,16,7,16,2,17,19,9,1,20,17,17,4,6]))
      

