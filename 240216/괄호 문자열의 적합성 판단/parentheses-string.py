def bracelet(string):
    array = []
    for i in range(len(string)):
        if string[i] == '(':
            array.append('(')
        else:
            if len(array) == 0:
                return False
            array.pop()
    
    if len(array) != 0:
        return False
    return True

string = input()
print("Yes" if bracelet(string) else "No")