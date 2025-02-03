def twoSum(nums, target):
   numbers = {}
   
   for i, value in enumerate(nums):
      diff = target - value
      if diff in numbers:
         return [numbers[diff] , i]
      numbers[value] = i
      