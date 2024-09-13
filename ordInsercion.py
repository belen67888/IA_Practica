ins = [70, 60, 50, 40, 30]

for i in range(1, len(ins)):
    key = ins[i]
    j = i -1
    while j >= 0 and key < ins[j]:
        ins[j + 1] = ins[j]
        j -= 1
    ins[j + 1] = key

print(ins)