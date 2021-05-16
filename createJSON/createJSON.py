import csv
class Node:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

nodes = []
edges = []
#Replace line 19 with line below to use a large input file
#csvFile = open("divisionGraph.csv")
csvFile = open("smallDivisionGraph.csv")
csvReader = csv.reader(csvFile)
for inputData in csvReader:
    if(len(inputData[1]) <= 4):
        nodes.append(Node(inputData[0],inputData[1],inputData[2]))
    else:
        edges.append(Edge(inputData[0], inputData[1], inputData[2]))

jsonFile = open("divisionJSON.json","w")    
jsonFile.write("{ \"nodes\": [\n")
for node in nodes:
    if(node != nodes[len(nodes) - 1]):
        jsonFile.write("{ \"name\":\"" + node.name + "\" ,\"x\":\"" + node.x + "\" ,\"y\":\"" + node.y + "\" } ,\n")
    else:
        jsonFile.write("{ \"name\":\"" + node.name + "\" ,\"x\":\"" + node.x + "\" ,\"y\":\"" + node.y + "\" }\n")
jsonFile.write("] ,\n")
jsonFile.write("\"edges\": [\n")
for edge in edges:
    if(edge != edges[len(edges) - 1]):
        jsonFile.write("{ \"start\":\"" + edge.start + "\" ,\"end\":\"" + edge.end + "\" ,\"weight\":\"" + edge.weight + "\" } ,\n")
    else:
        jsonFile.write("{ \"start\":\"" + edge.start + "\" ,\"end\":\"" + edge.end + "\" ,\"weight\":\"" + edge.weight + "\" }\n")
jsonFile.write("]\n")
jsonFile.write("}")
