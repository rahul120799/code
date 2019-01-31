digits = 0
number = int(input())
while (number > 0):
  number = number//10
  digits = digits + 1
print digits
