# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:22:09 2022

@author: sandeep
"""

import os, timeit
from math import log, sqrt
from pandas import DataFrame


dnames = []
voc_set = set()
corpus = []
inverted_index_map = {}

#utility to convert to pandas df
def pr_p(x):
    return DataFrame(x)
    
#utlity to tokenize a long string
def tokenize(s):
    return s.lower().replace(","," ",1000).replace("."," ",1000).replace("  "," ",10000).replace('"',' ',1000).replace('\n',' ',1000
        ).replace("'",' ',1000).replace("/",' ',1000).replace("\\"," ",1000).replace("("," ",1000).replace(";"," ",1000
        ).replace(")"," ",1000).replace("]"," ",1000).replace("["," ",1000).replace("-"," ",100).strip().split(" ")
    
#utility to make frequency dictionary
def freq(l):
	d = {}
	for x in l:
		d[x] = d.get(x,0)+1
	return d
    
#utility to read text file
def read_text(file):
    with open(file,'r') as f:
        return f.read()

'''changing directory to read corpus'''
path = input("enter folder path : ").strip()
curr_dir = str(os.getcwd())
new_path = ""
if "\\" in curr_dir:
	new_path = curr_dir + "\\" + path
elif "/" in curr_dir:
	new_path = curr_dir + "/" + path
os.chdir(new_path)
	

'''reading the documents in corpus'''
for i,file in enumerate(sorted(os.listdir())):
    if file.endswith(".txt"):
        filename = (file.replace('.txt',''))
        dnames.append(filename)
        file_path = f"{file}"
        content = read_text(file_path)
        words = tokenize(content)
        doc = freq(words)
        voc_set = voc_set.union(doc)
        corpus.append(doc)
        for w in doc:
        	if w not in inverted_index_map:
        		inverted_index_map[w] = [(i,doc[w])]
        	else:
        		inverted_index_map[w].append((i,doc[w]))
        		
vocab = sorted(list(voc_set))

M = len(vocab)
N = len(corpus)
print("\nLength of vocab : ",M)
print("No of documents : ",N)
print("Vocabulary is :\n",vocab)
print("Documents are :\n",dnames)
        		
inverted_index = DataFrame([(w, inverted_index_map[w]) for w in vocab])
print("inverted index\n", inverted_index)
	
	
        		




