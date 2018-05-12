#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 18:09:19 2018

@author: mayapetranova
"""

########################
## Q u e s t i o n 4 ##
#######################

import nltk
from nltk.tree import Tree
from nltk.draw.tree import TreeView

grammar = nltk.CFG.fromstring("""
S ->  NP VP 
S -> Aux NP VP 
S -> VP 
S -> IVP 
IVP -> IVerb NP NP 
IVP -> IVerb NP NP PP
NP -> NP PP
NP -> Pronoun 
NP -> Proper-Noun 
NP -> Det Nominal 
Nominal -> Noun 
Nominal -> Nominal Noun 
Nominal -> Nominal PP
VP -> Verb 
VP -> Verb NP 
VP -> Verb NP PP 
VP -> Verb PP 
VP -> VP PP 
PP -> Preposition NP
Det -> 'that' | 'this' | 'the' | 'a' 
Noun -> 'book' | 'flight' | 'meal' | 'money'  | 'seats'
Verb -> 'book' | 'include' | 'prefer'
Pronoun -> 'I' | 'she' | 'me' 
Proper-Noun -> 'Houston' | 'NWA' | 'Denver'
Aux -> 'does' 
Preposition -> 'from' | 'to' | 'on' | 'near' | 'through'
IVerb -> 'List'

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
    processSentence('List me the seats on the flight to Denver')

mainScript()

## For Drawing the CFG trees, uncomment lines 63-96
### Part 4b - visualising the trees with the initial grammar rules
#q4bs1 = Tree.fromstring('(S(IVP(IVerb List)(NP (Pronoun me))(NP(Det the)(Nominal(Nominal (Noun seats))(PP (Preposition on) (NP (Det the) (Nominal (Noun flight))))))(PP (Preposition to) (NP (Proper-Noun Denver)))))')
#q4bs2 = Tree.fromstring('(S(IVP(IVerb List)(NP (Pronoun me))(NP(Det the)(Nominal(Noun seats)))(PP(Preposition on)(NP(Det the)(Nominal(Nominal (Noun flight))(PP (Preposition to) (NP (Proper-Noun Denver))))))))')
#q4bs3 = Tree.fromstring('(S(IVP(IVerb List)(NP (Pronoun me))(NP(Det the)(Nominal(Nominal(Nominal (Noun seats))(PP(Preposition on)(NP (Det the) (Nominal (Noun flight)))))(PP (Preposition to) (NP (Proper-Noun Denver)))))))')
#q4bs4 = Tree.fromstring('(S(IVP(IVerb List)(NP (Pronoun me))(NP(Det the)(Nominal(Nominal (Noun seats))(PP(Preposition on))(NP(Det the)(Nominal(Nominal (Noun flight))(PP (Preposition to) (NP (Proper-Noun Denver)))))))))')

#TreeView(q4bs1)._cframe.print_to_file('q4bs1.ps')
#TreeView(q4bs2)._cframe.print_to_file('q4bs2.ps')
#TreeView(q4bs3)._cframe.print_to_file('q4bs3.ps')
#TreeView(q4bs4)._cframe.print_to_file('q4bs4.ps')

### Part 4c - visualising the trees after adding NP -> NP PP rule
#q4bs1add = Tree.fromstring('(S(IVP(IVerb List)(NP (Pronoun me))(NP(Det the)(Nominal(Nominal(Nominal (Noun seats))(PP(Preposition on)(NP (Det the) (Nominal (Noun flight)))))(PP (Preposition to) (NP (Proper-Noun Denver)))))))')
#q4bs2add = Tree.fromstring('(S(IVP(IVerb List) (NP (Pronoun me))(NP(Det the)(Nominal(Nominal (Noun seats))(PP(Preposition on)(NP(NP (Det the) (Nominal (Noun flight)))(PP (Preposition to) (NP (Proper-Noun Denver)))))))))')
#q4bs3add = Tree.fromstring('(S(IVP(IVerb List)(NP (Pronoun me))(NP(Det the)(Nominal(Nominal (Noun seats))(PP(Preposition on)(NP(Det the)(Nominal(Nominal (Noun flight))(PP (Preposition to) (NP (Proper-Noun Denver))))))))))')
#q4bs4add = Tree.fromstring('(S(IV(IVerb List)(NP (Pronoun me))(NP(NP(NP (Det the) (Nominal (Noun seats)))(PP (Preposition on) (NP (Det the) (Nominal (Noun flight)))))(PP (Preposition to) (NP (Proper-Noun Denver))))))')
#q4bs5add = Tree.fromstring('(S(IVP(IVerb List)(NP (Pronoun me))(NP(NP(Det the)(Nominal(Nominal (Noun seats))(PP(Preposition on)(NP (Det the) (Nominal (Noun flight))))))(PP (Preposition to) (NP (Proper-Noun Denver))))))')
#q4bs6add = Tree.fromstring('(S(IVP(IVerb List)(NP (Pronoun me))(NP(NP (Det the) (Nominal (Noun seats)))(PP(Preposition on) (NP (NP (Det the) (Nominal (Noun flight)))(PP (Preposition to) (NP (Proper-Noun Denver))))))))')
#q4bs7add = Tree.fromstring('(S(IVP(IVerb List)(NP (Pronoun me))(NP(NP (Det the) (Nominal (Noun seats)))(PP(Preposition on)(NP(Det the)(Nominal(Nominal (Noun flight))(PP (Preposition to) (NP (Proper-Noun Denver)))))))))')
#q4bs8add = Tree.fromstring('(S(IVP(IVerb List)(NP (Pronoun me))(NP(NP (Det the) (Nominal (Noun seats)))(PP (Preposition on) (NP (Det the) (Nominal (Noun flight)))))(PP (Preposition to) (NP (Proper-Noun Denver)))))')
#q4bs9add = Tree.fromstring('(S(IVP(IVerb List)(NP (Pronoun me))(NP(Det the)(Nominal(Nominal (Noun seats))(PP (Preposition on) (NP (Det the) (Nominal (Noun flight))))))(PP (Preposition to) (NP (Proper-Noun Denver)))))')
#q4bs10add = Tree.fromstring('(S(IVP(IVerb List)(NP (Pronoun me))(NP (Det the) (Nominal (Noun seats)))(PP(Preposition on)(NP(NP (Det the) (Nominal (Noun flight)))(PP (Preposition to) (NP (Proper-Noun Denver)))))))')
#q4bs11add = Tree.fromstring('(S(IVP(IVerb List)(NP (Pronoun me))(NP (Det the) (Nominal (Noun seats)))(PP(Preposition on)(NP(Det the)(Nominal(Nominal (Noun flight))(PP (Preposition to) (NP (Proper-Noun Denver))))))))')

#TreeView(q4bs1add)._cframe.print_to_file('q4bs1add.ps')
#TreeView(q4bs2add)._cframe.print_to_file('q4bs2add.ps')
#TreeView(q4bs3add)._cframe.print_to_file('q4bs3add.ps')
#TreeView(q4bs4add)._cframe.print_to_file('q4bs4add.ps')
#TreeView(q4bs5add)._cframe.print_to_file('q4bs5add.ps')
#TreeView(q4bs6add)._cframe.print_to_file('q4bs6add.ps')
#TreeView(q4bs7add)._cframe.print_to_file('q4bs7add.ps')
#TreeView(q4bs8add)._cframe.print_to_file('q4bs8add.ps')
#TreeView(q4bs9add)._cframe.print_to_file('q4bs9add.ps')
#TreeView(q4bs10add)._cframe.print_to_file('q4bs10add.ps')
#TreeView(q4bs11add)._cframe.print_to_file('q4bs11add.ps')