#!/usr/bin/env python3
from ete3 import Tree
import sys 

with open(sys.argv[1], 'r') as treefile:
	nwk_string = ''
	for line in treefile:
		nwk_string += line.rstrip("\n")

tree = Tree(nwk_string)

tree.set_outgroup(tree.get_common_ancestor("CELEG", "CINOP"))

print("CBRIG", "CREMA", tree.get_distance("CBRIG", "CREMA"))
print("CNIGO", "CREMA", tree.get_distance("CNIGO", "CREMA"))
print("CTROP", "CREMA", tree.get_distance("CTROP", "CREMA"))
print("CWALL", "CREMA", tree.get_distance("CWALL", "CREMA"))
print("CELEG", "CREMA", tree.get_distance("CELEG", "CREMA"))
print("CINOP", "CREMA", tree.get_distance("CINOP", "CREMA"))