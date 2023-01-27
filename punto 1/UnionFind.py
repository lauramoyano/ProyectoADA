import time 

import os

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

start_time = time.time()

# Nombre de la carpeta de entrada
input_folder = 'input'

# Nombre de la carpeta de salida
output_folder = 'output'

# Crear la carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Recorrer cada archivo en la carpeta de entrada
for filename in os.listdir(input_folder):
    nombre_archivo, extension = os.path.splitext(filename)
    outputfilename = nombre_archivo + "-salida.txt"
    # Crear la ruta completa del archivo
    input_path = os.path.join(input_folder, filename)
    # Crear la ruta completa de la carpeta de salida
    output_path = os.path.join(output_folder, outputfilename)

    # Abre el archivo de entrada y realiza alguna operación
    with open(input_path, 'r') as input_file:
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
                with open(output_path, "a") as output_file:
                    output_file.write(res + "\n")
    
                
end_time = time.time()

elapsed_time = end_time - start_time
print("El tiempo que demoro su ejecucion es", elapsed_time)