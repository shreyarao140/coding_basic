a = input(" give input")

w = a.split(" ")

for i in range(len(w)):
    w[i] = w[i].lower()

w.sort()
print(w)


