#Author: Samantha Zolin saz5193@psu.edu
#Section: 10  

def digit_sum(n):
  if (n == 0):
    return 0
  else:
    return n%10 + digit_sum(n//10)

def run():
  n = int(input("Enter an int: "))
  print(f"sum of digits of {n} is {digit_sum(n)}.")

if __name__== "__main__":
  run()


