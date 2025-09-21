nums = [0,1,0,3,12]

L = 0
R = 1

while R < len(nums):
   if nums[L] == 0 & nums[R] != 0:
         nums[L],nums[R] = nums[R], nums[L]
         L += 1
         R += 1

   elif nums[R] == 0:
         R += 1
   
   elif nums[L] != 0:
        L += 1

print(nums)