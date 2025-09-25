import math

n = 7
if n < 2:
    print("not prime")
else:
    for a in range(2, int(math.sqrt(n)) + 1): 
      if n % a == 0:
        print("not prime") 
        break
      else:
        print("prime")      
