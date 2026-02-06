def productExceptSelf(nums):
   n = len(nums)
   prefprod = [0] * n
   sufprod = [0] * n
   res = [0] * n

   print(nums)

   prefprod[0] = 1
   for i in range(1, n):
      prefprod[i] = prefprod[i-1] * nums[i-1] 

   print(prefprod)

   sufprod[n-1] = 1
   for i in range(n-2,-1,-1):
      sufprod[i] = sufprod[i+1] * nums[i+1]
   
   print(sufprod)

   
   for i in range(n):
      res[i] = prefprod[i] * sufprod[i]
       
   print(res)

productExceptSelf([-1,1,0,-3,3])

def productExceptSelfOptimal(nums):
   n = len(nums)
   pass

