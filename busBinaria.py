bina = [10, 20, 30, 40]
x = 20
low, high = 0, len(bina) - 1
found = -1

while low <= high:
    mid = (low + high) // 2
    if bina[mid] == x:
        found = mid
        break
    elif bina[mid] < x:
        low = mid + 1
    else:
        high = mid - 1

print(found)
