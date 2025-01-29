num = int(input("enter number to check armstrong number"))
sum = 0 
temp = num
num_digit = len(str(num))
while temp > 0:
    digit = temp % 10
    pow = digit**num_digit
    sum = sum + pow
    temp = temp//10
if num == sum:
    print(num, "is a arm no")
else:
    print(num, "is not a arm no")
