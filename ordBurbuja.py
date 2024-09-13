bur = [14, 25, 11, 22, 55]
a = len(bur)

for i in range(a):
    for j in range(0, a-i-1):
        if bur[j] > bur[j+1]:
            bur[j], bur[j+1] = bur[j+1], bur[j]

print(bur)