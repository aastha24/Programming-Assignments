if __name__ == '__main__':
    N = int(input())
    new = []
    for i in range (N):
        operation = list(input().split())
        if operation[0]=="insert":
            new.insert(int(operation[1]),int(operation[2]))
        elif operation[0]=="remove":
            new.remove(int(operation[1]))
        elif operation[0]=="append":
            new.append(int(operation[1]))
        elif operation[0]=="sort":
            new.sort()
        elif operation[0]=="pop":
            new.pop()
        elif operation[0]=="reverse":
            new.reverse()
        else: print(new)