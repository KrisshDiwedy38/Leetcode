def dnf(nums):
   m = 0
   l = 0 
   r = len(nums)-1
   while l < r:
      if nums[m] == 0:
            nums[m],nums[l] == nums[l], nums[m]
            m += 1
            l += 1
      elif nums[m] == 1:
            m += 1
      elif nums[m] == 2:
            nums[m],nums[r] == nums[r], nums[m]
            m += 1
            r -= 1

   return nums


dnf([2,0,2,1,1,0])