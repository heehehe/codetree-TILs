from collections import deque

dq = deque()

length = int(input())
for _ in range(length):
    cmd = input()
    if cmd.startswith("push_"):
        cmd, element = cmd.split(" ")
        if cmd == "push_front":
            dq.appendleft(int(element))
        else:
            dq.append(int(element))
        continue

    if cmd == "pop_front":
        print(dq.popleft())
    elif cmd == "pop_back":
        print(dq.pop())
    elif cmd == "size":
        print(len(dq))
    elif cmd == "empty":
        print(int(len(dq) == 0))
    elif cmd == "front":
        print(dq[0])
    elif cmd == "back":
        print(dq[-1])