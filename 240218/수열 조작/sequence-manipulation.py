from collections import deque

dq = deque()

for element in range(1, int(input())+1):
    dq.append(element)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])