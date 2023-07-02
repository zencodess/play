# Author: Sathya Sravya Vallabhajyosyula  
# Problem Description: 
# Consider 3 types of nodes, 
# Primary source - Can only act as a source (has only outgoing edge)
# Primary target - Can only act as target  (has only incoming edge)
# Intermediate node - Can act both as source and target (has incoming and outgoing edges)
# Given, 
#  (1) Set of trees - The root of each tree is a primary source, the leaves of the tree will be primary targets. Each tree need not be binary, it can be multi-nary 
#  (2) boolean golden matrix - matrix[i][j] represents presence of path between primary source 'i' and primary target 'j'
# Write a program to remove unnecessary edges in trees by reading through the golden matrix. 
#	If matrix[i][j] is True, keep the edges on the path from i to j.
#	If matrix[i][j] is False, remove any redundant edges on the path from i to j, thereby removing the path from i to j. 
# Below is the program to remove unnecessary connections of nodes, given existing connections and expected golden connections

# Scope for extension and discussion - Revealing, 
#   (1) how I can frame data and read into set of trees, given input connectivity in a high level config file
#   (2) how I can write valid tree connections left, into usable format for customers


import logging
logging.basicConfig(level=logging.INFO)


class Node:
  def __init__(self, nodeData, children=[]):
    self.data = nodeData
    self.children = children
    self.required = True
  
  def addChild(self, childNode):
    self.children.append(childNode)
  
  
class Tree:
  def __init__(self, root):
    self.root = root
    
  
def markingDFS(node, primarySrc, pathRequired, goldenMatrix):
  ''' Marking connection that are not valid in the tree, node-wise '''
  if not node:
    return 
  logging.info(f'Marking unwanted edges for node: {node.data}')
  
  for child in node.children:
    markingDFS(child, primarySrc, pathRequired, goldenMatrix)

  if node.children == [] and not goldenMatrix[primarySrc][node.data]:
    pathRequired = False
  node.required = pathRequired 
  
  
def removeUnwantedEdges(node, primarySrc, validConnections):
  '''  Remove unwanted children of node under consideration '''
  if not node:
    return
  
  children = node.children
  if not children and node.required:
    validConnections.append([primarySrc, node.data])
  
  for child in children:
    if not child.required:
      node.children.remove(child)

  for child in node.children:
    removeUnwantedEdges(child, primarySrc, validConnections)
    
  
def identifyUnwantedEdges(setOfTrees):
  ''' 
  Identify unwanted edges in given setOfTrees.
  Do a dfs on each tree, while traveling bottom up, mark Nodes as required or not.
  '''
  validConnections = []
  for tree in setOfTrees:
    logging.info(f'Identifying Unwanted Edges for tree with root: {tree.root.data}')
    markingDFS(tree.root, tree.root.data, True, goldenMatrix)
    removeUnwantedEdges(tree.root, tree.root.data, validConnections)
    
  logging.info(f'Valid connections identified: {validConnections}')
  return validConnections
    

def removeRedundantConnections(setOfTrees, goldenMatrix):
  validConnections = identifyUnwantedEdges(setOfTrees)
  return validConnections
  
  
def compareConnections(existing, golden):
  ''' Compare existing connections and golden connections '''
  for edge in existing:
    if not golden[edge[0]][edge[1]]:
      return False
  return True
  

######################################## Construct inputs ########################################################

def createInputSetOfTrees():
  '''
  Return 2 trees which can be depicted as below
  	     1 					
		/	  |    \
  2 	  3   	4
/	/	|	  |	    |	  \
5	6	7	  8	    9	  10	

						11	
					/	|	\
	    	12	13	14
      /	|
    15	16		
    
  Leaving existing primary source - primary target edge pairs as, 
      1 - 5, 1 - 6, 1 - 7, 1 - 8, 1 - 9, 1 - 10, 11 - 15, 11 - 16, 11 - 13, 11 - 14
  '''
  setOfTrees = set()
  
  node2 = Node(2, [Node(5), Node(6), Node(7)])
  node3 = Node(3, [Node(8)])
  node4, node12 = Node(4, [Node(9), Node(10)]), Node(12, [Node(15), Node(16)])
  node1 = Node(1, [node2, node3, node4])
  node11 = Node(11, [node12, Node(13), Node(14)])
  
  tree1, tree2 = Tree(node1), Tree(node11)
  setOfTrees.add(tree1)
  setOfTrees.add(tree2)
  return setOfTrees

def createInputGoldenMatrix():
  '''
  Let golden/ expected edges between primary sources and primary targets be
    1 - 7, 1 - 8, 1 - 9, 11 - 16
  '''
  goldenMatrix = [[False for i in range(17)] for i in range(17)]
  goldenMatrix[1][7], goldenMatrix[1][8], goldenMatrix[1][9] = True, True, True
  goldenMatrix[11][16] = True
  return goldenMatrix
##############################################################################################################  

if __name__ == "__main__":
  setOfTrees = createInputSetOfTrees()
  goldenMatrix = createInputGoldenMatrix()
  
  existingConnections = removeRedundantConnections(setOfTrees, goldenMatrix)
  print('SUCCESS!') if compareConnections(existingConnections, goldenMatrix) \
      else print('FAILED TO REMOVE CONNECTIONS, PLEASE CHECK INPUT SANITY!')
  
  
  
  
  
  
  
  
  
    



