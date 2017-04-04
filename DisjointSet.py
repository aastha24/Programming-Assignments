#Developer: Aastha Ananad

class DisjointSet:
    def __init__(self, n):
        self.p = list(range(n))

    def UNION(self, x, y):
        self.LINK(self.FIND(x), self.FIND(y))

    def LINK(self, x, y):
        self.p[x] = y

    def FIND(self, x):
        if x != self.p[x]:
            self.p[x] = self.FIND(self.p[x])
        return self.p[x]


def off_line_minimum(full_list, n):
    i = 0
    m = len([0 for element in full_list if element == 'E'])
    pos = [-1] * (n + 1)
    djset = DisjointSet(m + 1)
    for element in full_list:
        if (element == 'E'):
            i = i + 1
        else:
            pos[element] = i
    extracted = [None] * m
    for i in range(1, n + 1):
        j = djset.FIND(pos[i])
        if (m > j):
            extracted[j] = i
            djset.LINK(j, j + 1)
    return extracted


def main():
    n = 0
    full_list = []
    op_array = [line.strip() for line in open("hw3test.txt", 'r')]
    for i in op_array:
        if i.isdigit():
            full_list.append(int(i))
            n = n + 1
        else:
            full_list.append(i)

    ex_array = off_line_minimum(full_list, n)
    print("Extracted Array: ", ex_array)

if __name__ == '__main__':
    main()
