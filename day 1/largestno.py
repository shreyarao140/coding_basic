num1 = float(input("1st no"))
num2 = float(input("2nd no"))
num3 = float(input("3rd no"))

if num1 > num2 and num1 > num3 :
    print(num1, "is the largest")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest")
else:
    print(num3, "is the largest")