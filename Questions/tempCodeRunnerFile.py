def fac(num):
   if num < 1: return 1
   return (num * fac(num-1))

print(f"Factorial of 5 = {fac(5)}")

def reverse_string(stringg):
   return stringg[::-1]

print(f"Reverse of Krissh = {reverse_string('Krissh')}")

def print_patterns(n):
   for i in range(1,n+1):
      print("*" * i, end=" ")

      print(" " * n , end=" ")

      print("*" * ((n+1)-i), end=" ")
      print()
         

print_patterns(6)

def discount(price,disc):
   return price * (1-(disc/100))

print(discount(10000,25))

