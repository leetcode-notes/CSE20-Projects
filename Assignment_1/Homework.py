# Lecture 4 challenge:

# Modify the line of code below with the ??? to
# report the number of digits in a number represented
# in binary
# e.g. 6 is '110' in binary, and so the number of binary digits is 3
# See https://en.wikipedia.org/wiki/Binary_number

n = int(input("Enter a whole number: "))

# Calculate the number of digits in an integer (base 2).
count = 0
while n != 0:
  count = count + 1
  n = n // 2 

print("Number of digits in input in binary is: ", count)
