quic = [64, 25, 12, 22, 11]

left = [x for x in quic if x < quic[len(quic)//2]]
middle = [x for x in quic if x == quic[len(quic)//2]]
right = [x for x in quic if x > quic[len(quic)//2]]

quic = left + middle + right
print(quic)