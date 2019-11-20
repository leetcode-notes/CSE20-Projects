num = int(input())

final = 0  # final output
pointer = 100  # number that traverses all three numbers

for i in range(3):  # loops three times because it is a three digit number
    remainder = num % 10  # retrieves the last digit of the number
    final += remainder * pointer  # adds it to the final number
    num -= remainder  # reduces the original number by one digit
    num /= 10  # removes the 0 at the end of the digit
    pointer /= 10  # reduces the pointer accounting for the amount of digits

final = int(final)
print(final)
