def rec1(N): # Print something N times
   if N != 0:
      print(f" Hi! no. {N}")
      rec1(N-1)
   
def rec2(i , N): # 1 to N
   if i<1: return
   if i > N: return
   print(i)
   rec2(i+1,N)
   
def rec3(N): # N to 1
   if N < 1: return
   print(N)
   rec3(N-1)

def rec4(N): # Sum of first N
   if N < 1: return 0
   return(N + rec4(N-1))
   
# OR 

def rec5(N): # Sum = n (n +1) / 2
   return (N * ( N + 1)) // 2

def rec6(N): # Factorial
   if N < 1: return 1
   return(N * rec6(N-1))

def revArray(n, arr): # Reversing an Array
   p1 = 0
   p2 = n - 1
   while p1 < p2:
      arr[p1],arr[p2] = arr[p2],arr[p1]
      p1 += 1
      p2 -= 1
   return arr

def palindrome(string):
   p1 = 0
   p2 = len(string) - 1
   while p1 < p2:
      if not string[p1].isalnum():
         p1+=1
      elif not string[p2].isalnum():
         p2-=1
      elif string[p1].lower()!= string[p2].lower():
         return False
      else:
         p1+=1
         p2-=1
   return True

def fibo(n):
   if n <= 0:
        return []
   elif n == 1:
      return [0]
   elif n == 2:
      return [0, 1]
   else:
      series = fibo(n-1)
      series.append(series[-1] + series[-2])
      return series

if __name__ == "__main__":
   num = int(input("Enter any number: "))
   print(fibo(num))