#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 2 00:21:17 2018

@author: mayapetranova
"""
import nltk
from nltk import tree
from nltk.parse import pchart

def loadData(path):
	with open(path,'r') as f:
		data = f.read().split('\n')
	return data

def getTreeData(data):
	return map(lambda s: tree.Tree.fromstring(s), data)

# Main script
print("Loading data..")
data = loadData('parseTrees.txt')
print("Generating trees..")
treeData = getTreeData(data)
print("Done!")
print(" ")

########################
## Q u e s t i o n 6a ##
########################

#list to store all the extracted rules
treeProductions = []

# productions() function is used to extract the grammar rule for each sentence
for tr in treeData: # for tree in treeData
    treeProductions+=tr.productions()

S = nltk.Nonterminal("S")
grammar = nltk.induce_pcfg(S, treeProductions)

### Extracting PCFG to a text file
#grammar_PCFG = str(grammar)
#file = open('/Users/mayapetranova/Documents/QMUL/NLP/assignment_2/6/PCFG.txt', 'w')
#file.write(grammar_PCFG)
#file.close()

########################
## Q u e s t i o n 6b ##
########################


sentence = "show me the meals on the flight from Phoenix".split()
parser = pchart.InsideChartParser(grammar) 
for tp in parser.parse(sentence):
    print(tp)
    
## For Drawing the CFG trees, uncomment lines 59-80
#q6s1 = Tree.fromstring('(S(IVP(IVerb show)(NP (Pronoun me))(NP (Det the) (Nominal (Noun meals)))(PP(Preposition on)(NP(Det the)(Nominal(Nominal (Noun flight))(PP(Preposition from)(NP (Proper_Noun Phoenix))))))))')
#TreeView(q6s1)._cframe.print_to_file('q6s1.ps')
#q6s2 = Tree.fromstring('(S(IVP(IVerb show)(NP (Pronoun me))(NP(Det the)(Nominal(Nominal (Noun meals))(PP(Preposition on)(NP (Det the) (Nominal (Noun flight))))))(PP (Preposition from) (NP (Proper_Noun Phoenix)))))')
#TreeView(q6s2)._cframe.print_to_file('q6s2.ps')
#q6s3 = Tree.fromstring('(S(IVP(IVerb show)(NP (Pronoun me))(NP(NP (Det the) (Nominal (Noun meals)))(PP(Preposition on)(NP (Det the) (Nominal (Noun flight)))))(PP (Preposition from) (NP (Proper_Noun Phoenix)))))')
#TreeView(q6s3)._cframe.print_to_file('q6s3.ps')
#q6s4 = Tree.fromstring('(S(IVP(IVerb show)(NP (Pronoun me))(NP (Det the) (Nominal (Noun meals)))(PP(Preposition on)(NP(NP (Det the) (Nominal (Noun flight)))(PP (Preposition from) (NP (Proper_Noun Phoenix)))))))')
#TreeView(q6s4)._cframe.print_to_file('q6s4.ps')
#q6s5 = Tree.fromstring('(S(IVP(IVerb show)(NP (Pronoun me))(NP(Det the)(Nominal(Nominal(Nominal (Noun meals))(PP(Preposition on)(NP (Det the) (Nominal (Noun flight)))))(PP (Preposition from) (NP (Proper_Noun Phoenix)))))))')
#TreeView(q6s5)._cframe.print_to_file('q6s5.ps')
#q6s6 = Tree.fromstring('(S(IVP(IVerb show)(NP (Pronoun me))(NP(Det the)(Nominal(Nominal (Noun meals))(PP(Preposition on)(NP(Det the)(Nominal(Nominal (Noun flight))(PP(Preposition from)(NP (Proper_Noun Phoenix))))))))))')
#TreeView(q6s6)._cframe.print_to_file('q6s6.ps')
#q6s7 = Tree.fromstring('(S(IVP(IVerb show)(NP (Pronoun me))(NP(Det the)(Nominal(Nominal (Noun meals))(PP(Preposition on)(NP(NP (Det the) (Nominal (Noun flight)))(PP(Preposition from)(NP (Proper_Noun Phoenix)))))))))')
#TreeView(q6s7)._cframe.print_to_file('q6s7.ps')
#q6s8 = Tree.fromstring('(S(IVP(IVerb show)(NP (Pronoun me))(NP(NP (Det the) (Nominal (Noun meals)))(PP(Preposition on)(NP(Det the)(Nominal(Nominal (Noun flight))(PP(Preposition from)(NP (Proper_Noun Phoenix)))))))))')
#TreeView(q6s8)._cframe.print_to_file('q6s8.ps')
#q6s9 = Tree.fromstring('(S(IVP(IVerb show)(NP (Pronoun me))(NP(NP(Det the)(Nominal(Nominal (Noun meals))(PP(Preposition on)(NP (Det the) (Nominal (Noun flight))))))(PP (Preposition from) (NP (Proper_Noun Phoenix))))))')
#TreeView(q6s9)._cframe.print_to_file('q6s9.ps')
#q6s10 = Tree.fromstring('(S(IVP(IVerb show)(NP (Pronoun me))(NP(NP(NP (Det the) (Nominal (Noun meals)))(PP(Preposition on)(NP (Det the) (Nominal (Noun flight)))))(PP (Preposition from) (NP (Proper_Noun Phoenix))))))')
#TreeView(q6s10)._cframe.print_to_file('q6s10.ps')
#q6s11 = Tree.fromstring('(S(IVP(IVerb show)(NP (Pronoun me))(NP(NP (Det the) (Nominal (Noun meals)))(PP(Preposition on)(NP(NP (Det the) (Nominal (Noun flight)))(PP(Preposition from)(NP (Proper_Noun Phoenix))))))))')
#TreeView(q6s11)._cframe.print_to_file('q6s11.ps')