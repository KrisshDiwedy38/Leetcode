def longestConsecutive(nums):
   nums = list(set((nums)))
   max_seq = []
   local_seq = 1
   print(nums)
   for i in range(1, len(nums)):
      print(nums[i])
      if (nums[i-1] + 1) == nums[i]:
         local_seq += 1
         print("Local seq increased")
      else:
         max_seq.append(local_seq)
         print("Seq interepted, past score appended")
         local_seq = 1
   max_seq.append(local_seq)
   return max(max_seq)

print(longestConsecutive([100,4,200, 1,3,2]))