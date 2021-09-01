import networkx as nx 
import matplotlib.pyplot as plt
import os
import numpy



def getAllTextFilesinFolder():
    files=[]
    for filename in os.listdir(os.getcwd() + "/Files"):
        if filename.endswith('.txt'):
            files.append(filename.strip('.txt'))
    return files

def getNodesList(Matrix=[]):
    list=[]
    for r in range(0,len(Matrix)):
        for c in range(0,len(Matrix[r])):
            if Matrix[r][c]>0:
                list.append((r+1,c+1))
            else :
                list.append((r + 1,r+1))

    return list

FilesNames = getAllTextFilesinFolder()
size = len(FilesNames)
__2DArray__ = numpy.zeros((size, size))
# print(__2DArray__)
for file in FilesNames:
    data = open('Files/' + file + '.txt').read().split(' ')
    # print(data)
    for item in data:
        try:
            int(item)
            n = int(file) - 1
            m = int(item) - 1
            if n != m and n < size and m < size:
                __2DArray__[n][m] = 1
        except:
            continue
print(__2DArray__)



G = nx.Graph()

plt.figure(figsize=(6,6))
G.add_edges_from(getNodesList(__2DArray__))


nx.draw_networkx( nx.to_directed(G))

plt.savefig('static/graph.png', transparent=True)
# plt.subplot(211)
# plt.show()
