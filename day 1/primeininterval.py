low = int(input("entter low no"))
up = int(input("entter up no"))

for num in range(low, up+1):
    if num > 1 :
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, "is a prime no")