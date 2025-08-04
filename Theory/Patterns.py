def pattern1(n): #5x5 * 
   for i in range(n):
      for j in range(n):
         print("*",end="")
      print()

def pattern2(n): #right * triangle
   for i in range(n+1):
      for j in range(i):
         print("*", end="")
      print()

def pattern3(n): #right numbered triangle ( 1 12 123)
   for i in range(1,n+1):
      for j in range(1,i+1):
         print(j, end="")
      print()

def pattern4(n): #right numbered triangle ( 1 22 333)
   for i in range(1,n+1):
      for j in range(1,i+1):
         print(i, end="")
      print()

def pattern5(n): #inverted right * triangle
   for i in range(n,0,-1):
      for j in range(i):
         print("*", end="")
      print()

def pattern6(n): #inverted right numbered triangle
   for i in range(n,0,-1):
      for j in range(1,i+1):
         print(j, end="")
      print()

def pattern7(n): # Pyramid
   for i in range(1,n+1):
      spaces = ' ' * (n - i)
      stars = '*' * (2 * i - 1)
      print(spaces + stars)

def pattern8(n): # Inverted Pyramid
   for i in range(n, 0,-1):
      spaces = ' ' * (n - i)
      stars = '*' * (2 * i - 1)
      print(spaces + stars)

def pattern9(n): # Joint Pyramid
   pattern7(n)
   pattern8(n)

def pattern10(n): # Joint right triangles
   for i in range(1,n*2):
      if i < n:
         print("*" * i)
      else:
         print("*"*(n*2 - i))

def pattern11(n): # Right triangle (1 01 101)
   for i in range(1,n+1):
      if i % 2 == 0:
         start = "even"
      else:
         start = "odd"
      for j in range(1,i+1):
         if start == "odd":
            if j %2 == 0:
               print(0,end="")
            else:
               print(1,end="")
         else:
            if j %2 == 0:
               print(1,end="")
            else:
               print(0,end="")
      print()

def pattern12(n): # Right triangle + mirrored
   for i in range(1,n+1):
      for j in range(1,i+1):
         print(j,end="")
      print(" " * (n-i)*2,end="")
      for j in range(i,0,-1):
         print(j,end="")
      print()

def pattern13(n): # Alphabet right triangle
   for i in range(1,n+1):
      for j in range(i):
         asc = 65 + j
         print(chr(asc), end="")
      print()
      
def pattern14(n): # Alphabet right inverter triangle
   for i in range(n,0,-1):
      for j in range(i):
         asc = 65 + j
         print(chr(asc), end="")
      print()

def pattern15(n): # Alphabet right triangle (A BB CCC)
   for i in range(0,n):
      for j in range(i+1):
         asc = 65 + i
         print(chr(asc),end="")
      print()

def pattern16(n): # Alphabet mirror pyramid (A ABA ABCBA)
   for i in range(n):
      print(" "* (n-i), end="")
      asc = 65
      for j in range(i*2+1):
         mid = (i*2 + 1) // 2
         print(chr(asc),end="")
         if j+1 <= mid:
            asc += 1
         else:
            asc-= 1
      print()
         
def pattern17(n): # Alphabet right triangle (E DE CDE)
   for i in range(n-1,-1,-1):
      asc = 65
      for j in range(i,n):
         print(chr(asc+j),end="")
      print()
         
def pattern18(n): # Diamond in middle
   for i in range(n,0,-1):
      for j in range(1,i+1):
         print("*",end="")
      print(" " * (n-i)*2,end="")
      for j in range(i,0,-1):
         print("*",end="")
      print()
   for i in range(1,n+1):
      for j in range(1,i+1):
         print("*",end="")
      print(" " * (n-i)*2,end="")
      for j in range(i,0,-1):
         print("*",end="")
      print()

def pattern19(n): # Joint right triangle mirrored
   for i in range(1,n+1):
      for j in range(i):
         print("*", end="")
      print(" " * (n-i) * 2, end="")
      for j in range(i):
         print("*", end="")
      print()
   for i in range(n-1, 0, -1):
      for j in range(1,i+1):
         print("*", end="")
      print(" " * (n-i)*2 , end="")
      for j in range(i):
         print("*", end="")
      print()

def pattern20(n): # Right triangle 1 to n numbers
   num = 0
   for i in range(1,n+1):
      for j in range(1,i+1):
         num += 1
         print(num,end=" ")
      print()

def pattern21(n): # Empty box
   for i in range(n):
      for j in range(1,n+1):
         if i == 0 or i == n-1 or j == 1 or j == n:
            print("*", end="")
         else:
            print(" ",end="")
      print()

def pattern22(n): #Concentric Squares
   for i in range(0,n*2-1):
      for j in range(0,n*2-1):
         top = i
         bottom = j 
         right = (2*n-2) - j
         left = (2*n-2) - i

         print( n - (min(min(top,bottom) , min(left,right))),end=" ")

         
      print()

def main(n):
   pattern5(n)

if __name__ == "__main__":
   main(n = 5) 