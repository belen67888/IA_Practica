sel = [75, 66, 33, 12, 22, 11]

for i in range(len(sel)):
    min_sel = i
    for j in range(i+1, len(sel)):
        if sel[j] < sel[min_sel]:
            min_sel = j
    sel[i], sel[min_sel] = sel[min_sel], sel[i]

print(sel)