merg = [64, 25, 12, 22, 11]


mid = len(merg) // 2
L = merg[:mid]  
R = merg[mid:]  

L.sort()  
R.sort()  

i = j = k = 0

while i < len(L) and j < len(R):
    if L[i] < R[j]:
        merg[k] = L[i]
        i += 1
    else:
        merg[k] = R[j]
        j += 1
    k += 1

while i < len(L):
    merg[k] = L[i]
    i += 1
    k += 1

while j < len(R):
    merg[k] = R[j]
    j += 1
    k += 1

print(merg) 
