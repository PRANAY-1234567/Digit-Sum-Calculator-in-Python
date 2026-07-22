num = int(input("Enter any number : "))

digit_sum = 0

while num > 0:
    digit = num % 10
    num //= 10
    digit_sum += digit

print("The digit sum is", digit_sum)