Problem Description: 
Consider 3 types of nodes, 
Primary source - Can only act as a source (has only outgoing edge)
Primary target - Can only act as target  (has only incoming edge)
Intermediate node - Can act both as source and target (has incoming and outgoing edges)
Given, 
 (1) Set of trees - The root of each tree is a primary source, the leaves of the tree will be primary targets. Each tree need not be binary, it can be multi-nary 
 (2) boolean golden matrix - matrix[i][j] represents presence of path between primary source 'i' and primary target 'j'
Write a program to remove unnecessary edges in trees by reading through the golden matrix. 
	If matrix[i][j] is True, keep the edges on the path from i to j.
	If matrix[i][j] is False, remove any redundant edges on the path from i to j, thereby removing the path from i to j. 
// Program to remove unnecessary connections of nodes, given existing connections and expected golden connections
