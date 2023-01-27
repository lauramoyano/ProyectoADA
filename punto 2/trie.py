import os
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = ""
        self.frecuency = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
              current.children[char] = TrieNode()
            current = current.children[char]
            current.frecuency += 1
        current.is_end_of_word = True
        current.word = word
 
    def getword(self, tnode):
      if  tnode.is_end_of_word:
        return tnode.word
      else:
        actualFre = 0
        maxFre = 0 
        keylist = sorted(tnode.children)
        maxObj = tnode.children[keylist[0]]
        while  keylist:
          actObj = tnode.children[keylist[0]]
          actualFre = actObj.frecuency
          if (actualFre > maxFre ):
            maxFre = actualFre
            maxObj = actObj
          keylist.pop(0)
        return self.getword(maxObj)

    def predict_word(self, prefix):
        current = self.root
        for char in prefix:
          if char not in current.children:
            return self.getword(current)
          else:
            current = current.children[char]
        if current.is_end_of_word:
          return current.word
        else:
          return self.getword(current)


# Nombre de la carpeta de entrada
input_folder = 'input'

# Nombre de la carpeta de salida
output_folder = 'output'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
  nombre_archivo, extension = os.path.splitext(filename)
  outputfilename = nombre_archivo + "-salida.txt"
  # Crear la ruta completa del archivo
  input_path = os.path.join(input_folder, filename)
  # Crear la ruta completa de la carpeta de salida
  output_path = os.path.join(output_folder, outputfilename)

  with open(input_path, "r") as input_file:
      n = int(input_file.readline())
      trie = Trie()
      results = []
      
      # Abrir el archivo de salida antes del bucle
      with open(output_path, 'a') as output_file:
          for _ in range(n):
              op, word = input_file.readline().split()
              if op == '1':
                  trie.insert(word)
              elif op == '2':
                  prefix = trie.predict_word(word)
                  results.append(prefix)
                  output_file.write(prefix + '\n')
   

   

