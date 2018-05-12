#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 17:56:32 2018

@author: mayapetranova
"""

########################
## Q u e s t i o n 3 ##
#######################

import nltk
from nltk.corpus import treebank
from nltk.draw.tree import TreeView 
from nltk.tree import Tree

sentence22 = treebank.parsed_sents('wsj_0003.mrg')[21]
sentence7 = treebank.parsed_sents('wsj_0003.mrg')[6]
sentence13 = treebank.parsed_sents('wsj_0004.mrg')[12]

grammar = nltk.CFG.fromstring("""

S -> PP-TMP NP-SBJ VP
PP-TMP -> IN NP
NP-SBJ -> DT NNP NNP NNP
NP -> NNP 
VP -> VBD NP PP-CLR
NP -> DT JJ NN
PP-CLR -> IN NP
NP -> NP PP
NP -> ADJP NNS
ADJP -> RB DT
PP -> IN NP
NP -> NN

S -> NP-SBJ VP
NP-SBJ -> EX
VP -> VBZ NP-PRD PP-LOC ADVP-TMP
NP-PRD -> DT NN
PP-LOC -> IN NP
NP -> PRP NNS
ADVP-TMP -> RB

S -> NP-SBJ VP
NP-SBJ -> DT JJ NN NNS
VP -> VBP ADVP-TMP VP
ADVP-TMP -> RB
VP -> VBG NP
NP -> QP NN
QP -> RB IN CD

NNP -> 'Environmental' | 'Protection' | 'Agency' | 'July'
IN -> 'In' | 'of' | 'on' | 'in' | 'over'
DT -> 'the' | 'a' | 'all' | 'no' | 'The'
VBD -> 'imposed'
JJ -> 'gradual' | 'top'
NN -> 'ban' | 'asbestos' | 'asbestos' | '%' | 'money'
RB -> 'virtually' | 'now' | 'well' | 'currently'
NNS -> 'uses' | 'funds' | 'products'
EX -> 'There'
PRP -> 'our'
VBZ -> 'is'
CD -> '9'
VBG -> 'yielding'
VBP -> 'are'

""")

parser = nltk.ChartParser(grammar)

def allParses(sentenceList):
	return parser.parse(sentenceList)

def printParses(parses):
	for tree in parses:
		print(tree)

def processSentence(sentence):
	sentenceList = sentence
	if isinstance(sentence,str):
		sentenceList = sentence.split(' ')
	print ('Original sentence: ' + ' '.join(sentenceList))
	printParses(allParses(sentenceList))

def mainScript():
    #Preprocessing Sentence 22
    processSentence('In July the Environmental Protection Agency imposed a gradual ban on virtually all uses of asbestos') 
    #Preprocessing Sentence 7
    processSentence('There is no asbestos in our products now')
    #Preprocessing Sentence 13
    processSentence('The top money funds are currently yielding well over 9 %')

mainScript()

#Drawing the CFG trees for the given sentences
TreeView(sentence22)._cframe.print_to_file('s22.ps')
sentence22_after_adding_rules_in_grammar = Tree.fromstring('(S(PP-TMP (IN In) (NP (NNP July)))(, ,)(NP-SBJ (DT the) (NNP Environmental) (NNP Protection) (NNP Agency))(VP(VBD imposed)(NP(NP (DT a) (JJ gradual) (NN ban))(PP (IN on) (NP (ADJP (RB virtually) (DT all)) (NNS uses))))(PP-CLR (IN of) (NP (NN asbestos))))(. .))')
TreeView(sentence22_after_adding_rules_in_grammar)._cframe.print_to_file('s22b.ps')

TreeView(sentence7)._cframe.print_to_file('s7.ps')
TreeView(sentence13)._cframe.print_to_file('s13.ps')


