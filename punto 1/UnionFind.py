class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
        
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parents[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parents[y_root] = x_root
        else:
            self.parents[y_root] = x_root
            self.rank[x_root] += 1
    
    def is_same_group(self, x, y):
        return self.find(x) == self.find(y)
        
with open("./input3.txt", "r") as input_file:
    n, q = map(int, input_file.readline().split())
    uf = UnionFind(n)

    for _ in range(q):
        query, a, b = map(int, input_file.readline().split())
        if query == 1:
            uf.union(a - 1, b - 1)
        elif query == 2:
            for i in range(a - 1, b):
                uf.union(i, a - 1)
        elif query == 3:
            res = "true" if uf.is_same_group(a - 1, b - 1) else "false"
            with open("./output3.txt", "a") as output_file:
                output_file.write(res + "\n")