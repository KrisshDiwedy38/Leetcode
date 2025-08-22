nums = [1,2,3,4,5,6]

max = nums[len(nums) - 1] + 1

L = 0
R = len(nums) - 1
for i in range(len(nums)-1):
   if i % 2 == 0:
      nums[i] = nums[i] + (nums[R] % max * max)
      R -= 1
   else:
      nums[i] = nums[i] + (nums[L] % max * max)
      L += 1

print(nums)

for i in range(len(nums)-1):
   nums[i] = nums[i] // max

print(nums)

