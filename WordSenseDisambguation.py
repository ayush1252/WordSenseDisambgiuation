from sets import Set
import networkx as nx
import pylab as plt
import math

from networkx.drawing.nx_agraph import graphviz_layout
from nltk.corpus import wordnet as wn

drink=wn.synsets('drink')
milk=wn.synsets('food')
graph = nx.DiGraph()


drink=Set(drink)
milk=Set(milk)
senses=milk

log=drink

for x in senses:
	log.add(x)

seen=Set()


for x in drink:   
	graph.add_node(x.name,level=1)

for x in milk:
	graph.add_node(x.name,level=10)


def pairwise(it):
    it = iter(it)
    while True:
        yield next(it), next(it)

def func(abc,x):
	global senses
	global graph
	if(len(abc)>=4):
		return
	else:


		for i in x:
			tempelementsyet=Set(abc)
			tempelementsyet.add(i)
			if(i in abc):
				continue
			elif(i in senses):
				print "Found a path:"
				print abc ,i
				print "\n"
				abc.add(i)
				for m in abc:
					graph.add_node(m.name)
				for a,b in pairwise(abc):
					graph.add_edge(a.name,b.name)
				senses.update(abc)
				continue
			elif(i in seen):
				continue
			else:
				seen.add(i)
				hypo1=i.hyponyms()
				hype1=i.hypernyms()
				xyz1=wn.synsets(i.name())
				func(tempelementsyet,hypo1)
				func(tempelementsyet,hype1)
				func(tempelementsyet,xyz1)






for x in drink:
	hype=x.hypernyms()
	hypo=x.hyponyms()
	xyz=wn.synsets(x.name())

	elementsyet=Set([x])
	seen.add(x)
	func(elementsyet,hypo)
	func(elementsyet,hype)
	func(elementsyet,xyz)
	

nx.draw(graph, with_labels=True,pos=graphviz_layout(graph), node_size=3600, cmap=plt.cm.Blues,
        node_color=range(len(graph)),
        prog='dot',label='val')


#TOCode:- Djikstra Algorithm  to find shortest length in pytho n 
def djikstra(graph,x,y):
	if nx.has_path(graph,x,y):
		return nx.shortest_path_length(graph,x,y,1)
	else:
		return graph.number_of_nodes()


def calcdegree(hx):
	dict={}
	for x in hx:
		dict[x]=graph.degree(x)

	return dict

def entropy(degree):
	sum=0.0
	for x in degree:
		degree[x]=float(float(degree[x])/float(graph.number_of_edges()))
		if degree[x]!=0.0:
			degree[x]=float(degree[x])*float(math.log(degree[x]))
		else:
			degree[x]=0
		sum=sum+degree[x]
		sum=sum*-1
		sum=sum/float(math.log(graph.number_of_nodes()))

	return sum


dict=nx.degree_centrality(graph)
print ("\nDegree Centrality\n")

for i in dict:
    print i, dict[i]

print("\nBetweeeness\n")
dict=nx.betweenness_centrality(graph,normalized=True)

for i in dict:
    print i, dict[i]

print("\nPagerank\n")
dict=nx.pagerank(graph)
for i in dict:
    print i, dict[i]

print("\nHits\n")
hx,a=nx.hits(graph)

for i in hx:
    print i, hx[i]

print("\nCloseness\n")

hx=nx.closeness_centrality(graph)

for i in hx:
    print i, hx[i]

print("\nGLOBAL MEASURES\n")

degree=calcdegree(hx)
print("\nEntropy")
allentropy=entropy(degree)
print allentropy


edgedensity=nx.density(graph)
print("\nEdge Density")
print edgedensity


totalsum=0
for x in graph.nodes():
	for y in graph.nodes():
		val=djikstra(graph,x,y)
		totalsum=totalsum+val

print("\nCompactness")
max=graph.number_of_nodes()*graph.number_of_nodes()*(graph.number_of_nodes()-1)
min=graph.number_of_nodes()*(graph.number_of_nodes()-1)
compactness=float(max-totalsum)/float(max- min )
print compactness

plt.show()
print senses
