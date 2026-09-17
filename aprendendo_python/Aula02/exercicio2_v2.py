x = 1
y = 1
z = 1
n = 2

arr = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if n != (i + j + k):
                arr.append([i,j,k])
    
print(arr)
