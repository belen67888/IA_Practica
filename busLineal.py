busLin = [20]
busLin = [30]
busLin = [40]
busLin = [50]

x = 50
y = 0
while y < len(busLin) and busLin[y] !=x:
    y += 1

if y < len(busLin):
    print(y)
else: 
    print(-1)