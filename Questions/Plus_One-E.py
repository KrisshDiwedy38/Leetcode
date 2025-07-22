def plusOne(digits):
   number = 0
   for i in range(0,len(digits)):
      number += digits[i] * (10 **( len(digits) - i - 1))
   
   number += 1 
   new_digits = []
   
   while number != 0:
      new_digits.append(number%10)
      number //= 10
      
   return new_digits[::-1]

