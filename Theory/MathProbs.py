import math

def floatToInt(float_num):
   int_num = int(str(float_num).split('.')[0]+str(float_num).split('.')[1])
   return int_num

def maths1(float_num): # Count the number of digits
   int_num = int(str(float_num).split('.')[0]+str(float_num).split('.')[1])
   digits = round(math.log10(int_num) + 1)
   return(f"Digits in {float_num} : {digits}")

def maths2(float_num): # Reverse the number
   float_numbers = str(float_num).split('.')
   if float_numbers[1] == '0':
      decimal = 0
      int_num = int(float_numbers[0])      
   else:
      decimal = len(float_numbers[0])
      int_num = int(float_numbers[0] + float_numbers[1])
   revNum = 0
   while int_num > 0:
      last_digit = int_num % 10
      revNum = (revNum * 10) + last_digit 
      int_num = int_num // 10
   return(revNum/10**decimal)

def maths3(float_num): # Checking for palindrome
   revNum = maths2(float_num)
   if revNum == float_num:
      return("Palindrome")
   else:
      return("Not Palindrome")

def maths4(a, b):  # GCD
    if a == 0 or b == 0:
        return max(a, b)

    if a == b:
        return a

    if a > b:
        return maths4(a - b, b)
    else:
        return maths4(a, b - a)

def maths5(a,b): # LCM = |a * b| // GCD (a,b)
   if a == 0 or b == 0:
      return 0
   else:
      return f" LCM = { abs(a*b) // maths4(a,b)}"

def maths6(number): # Armstrong abc = a^3 + b^3 + c^3 ( 3 = len(abc)) 
   length = len(str(number))
   sum = 0
   while number > 0:
      last_digit = number % 10
      sum == last_digit ** length
      number = number // 10

   if sum == number:
      return("Yes")
   else:
      return('No')

def maths7(number): # All Divisors
   root = int(math.sqrt(number))
   divs = []
   for i in range(1,root+1):
      if number % i == 0:
         divs.append(i)
         if i != number // i:
            divs.append(number // i) 
      else:
         continue
   return sorted(divs)

def maths8(number): # Check for prime
   if number == 0:
      return 0
   if number == 1:
      return 1
   else: 
      divs = maths7(number)
      return True if len(divs) == 2 else False

def main():
   inputs  = int(input("Enter any number: "))
   print(maths7(inputs))

if __name__ == "__main__":
   main()