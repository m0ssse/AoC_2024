class Graph:
    def __init__(self):
        self.neighbs = {}
        self.nodes = set()

    def add_edge(self, a, b):
        if a not in self.neighbs:
            self.neighbs[a] = set()
        if b not in self.neighbs:
            self.neighbs[b] = set()
        self.neighbs[a].add(b)
        self.neighbs[b].add(a)
        self.nodes.add(a)
        self.nodes.add(b)
    
def part1(graph):
    res=0
    allnodes = sorted(list(graph.nodes))
    for i in range(len(allnodes)):
        c1 = allnodes[i]
        for j in range(i):
            c2 = allnodes[j]
            for k in range(j):
                c3 = allnodes[k]
                if c1 in graph.neighbs[c2] and c1 in graph.neighbs[c3] and c2 in graph.neighbs[c3] and (c1[0]=="t" or c2[0]=="t" or c3[0]=="t"):
                    res+=1
    print(res)
    cliques = set()
    R = set()
    P = graph.nodes.copy()
    X = set()
    bors_kerbosch(R, P, X, graph, cliques)
    print(",".join(max(cliques, key=len)))

def bors_kerbosch(R, P, X, graph, cliques):
    if not P and not X:
        cliques.add(tuple(sorted(R)))
        return
    for v in list(P):
        bors_kerbosch(R.union(set([v])), P.intersection(graph.neighbs[v]), X.intersection(graph.neighbs[v]), graph, cliques)
        P.remove(v)
        X.add(v)

fname = "day23_input.txt"
g = Graph()
with open(fname) as file:
    for line in file:
        a, b = line.strip().split("-")
        g.add_edge(a, b)

part1(g)