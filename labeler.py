## -----------------------------------------------------
## Graceful labeler program
## Author: Atilio Gomes Luiz
## Date: August 2020
## ---------------------------
## Program that reads the list of adjacency of a given 
## graph and prints all of its graceful labellings.
## It is assumed that the vertex set of the graph is 
## V(G) = {0,1,...,|V(G)|-1}
## ---------------------------
## Input: a file called edges.txt with the list of edges
## Output: a file called labelings.txt containg a list of 
## the vertex labels for each of the graceful labelings 
## found, if any.
## -----------------------------------------------------

import sys
import ast

def is_safe(G,vertex,labelling,l,edge_labels):
	""" A label is safe if it was not assigned to a previous vertex
	and if it does not generate a repeated edge label. """
	if l in labelling:
		return False
	
	aux = list()
	for neighbour in G[vertex]:
		if labelling[neighbour] != -1:
			value = abs(l - labelling[neighbour])
			if (value in edge_labels) or (value in aux):
				return False
			aux.append(value)
			
	return True

		
def generate_labelling(G, edges, labelling, index, edge_labels):
	""" A recursive function that searches for a graceful labelling."""
	if labelling.count(-1) == 0:
		print labelling
		return True
		
	for l in xrange(0,len(edges)+1):
		if is_safe(G, index, labelling, l, edge_labels):
			labelling[index] = l
			
			for neighbour in G[index]:
				if labelling[neighbour] != -1:
					edge_labels.add(abs(labelling[index]-labelling[neighbour]))
			
			generate_labelling(G,edges,labelling,index+1,edge_labels)
			
			## backtrack
			labelling[index] = -1 
			for neighbour in G[index]:
				if labelling[neighbour] != -1:
					edge_labels.discard(abs(l-labelling[neighbour]))
				
	return False
				

if __name__ == "__main__":
	# 0-indexed labelling 
	
	## Open file with read only permit
    file_in = open('edges.txt')
    ## Open file with write permit
    file_out  = open("labellings.txt",'w')
    sys.stdout = file_out
    
    ## Read the first line of input file
    edges = file_in.readline().rstrip('\n')
    edges = ast.literal_eval(edges)
    
    ## Create graph G
    G = dict()
    for e in edges:
		if e[0] not in G:
			G[e[0]] = []
		if e[1] not in G:
			G[e[1]] = []
		G[e[0]].append(e[1])
		G[e[1]].append(e[0])
		
	## list with the final labelling
    labelling = [-1]*len(G)    
    
    generate_labelling(G, edges, labelling, 0, set())
    
    file_out.close()
    file_in.close()
    
    
