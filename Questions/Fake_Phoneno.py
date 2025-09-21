n = int(input("-> "))

def validity(pno):
   if pno.startswith("+91"):
      nums = pno.split(" ")
      if len(nums[2]) == 5:
         if nums[1].isdigit() and nums[2].isdigit():
            return True
      return "False" 

   elif pno.startswith("0"):
      nums = pno.split(" ")
      if len(nums[1]) == 5:
         if nums[0].isdigit() and nums[1].isdigit():
            return True
      return "False"
   


for i in range(n):
   phone_number = input("pno -> ")

   print(f"{phone_number} is {validity(phone_number)}")


