num = int(input("entter no"))
for i in range(2, num):
    if num % i == 0 :
        print(num, "is not a prime number")
    else:
        print(num, "is a prime no")