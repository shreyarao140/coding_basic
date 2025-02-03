a = [[1,5,7],
     [2,4,6],
     [7,2,3]]

b = [[1,5,7],
     [2,4,6],
     [7,2,3]]

results = [[0,0,0],
           [0,0,0],
           [0,0,0]]

for i in range (len(a)):
    for j in range(len(b[0])):
            for k in range(len(b)):
                results[i][j] +=a[i][k]* b[k][j]

for i in results:
     print(i)