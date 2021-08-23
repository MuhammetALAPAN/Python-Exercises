import sys

def pow(num):
  return num ** 2

try:
  n = int(input("enter desired num: "))

except Exception as e:
  print("Oops there is an error: ", e.__class__)

print("Result: ", pow(n))