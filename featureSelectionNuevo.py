# -------------------------------------------------
#  Universidad Simón Bolívar
#  Inteligencia Artificial II
#  Prof. Ivette Carolina Martinez
#
#  Autores: Jorge Marcano         # Carnet : 11-10566
#           Maria Victoria Jorge  # Carnet : 11-10495
#           Fabio Castro          # Carnet : 10-10132
#
# Proyecto Final 
# -------------------------------------------------
# Programa para obtener las features dada una lista de terminos (topicos).

import re
import math

# fij: total occurrences of the term i in the document j.
# fdj: total number of terms occurring in document j.
# fti: total number of documents in which the term i occurs. 
def obtainFeatures(topics,docs):
	fdj = [] # De la forma [#totalEnDoc1,#totalEnDoc2...]
	fti = {} # De la forma {t1 : #,t2: #...}
	fij = {} # De la forma {t1 : [#paraDoc1,#paraDoc2...],t2: [#paraDoc1,#paraDoc2...]}

	totalDocs = len(docs)

	topicos = []
	i = 0
	for t in topics :
		topicos.append(i)
		i += 1

	for t in topicos :
		fti[t] = 0
		fij[t] = []

	for t in topicos:
		for d in docs :
			fij[t].append(0)

	for d in docs :
		fdj.append(0)

		# Cambiar ./UserTests por ./CleanUserDocs para probar casos serios
		document = open("./CleanUserDocs/"+str(d)+".txt").read()

		# Calculo de fdj nuevo
		for line in document :
			for word in line.split() :
				fdj[d-1] += 1

		for t in topicos :
			for word in topics[t] :
				count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), document,re.IGNORECASE))
				fij[t][d-1] += count

	for t in topicos :
		for doc in fij[t] :
			if doc > 0 :
				fti[t] = fti[t]+1

	# print(fdj)
	# print("")
	# print("total number of terms occurring in document j.")
	# print(fdj)
	# print("")
	# print("total number of documents in which the term i occurs. ")
	# print(fti)
	# print("")
	# print("total occurrences of the term i in the document j.")
	# print(fij)
	# print("")

	# DESCOMENTAR A PARTIR DE AQUI.
	
	# De la forma {t1 : [#paraDoc1,#paraDoc2...],t2: [#paraDoc1,#paraDoc2...]}
	termOcurrence = fij

	# # De la forma {t1 : [#paraDoc1/#totalEnDoc1,#paraDoc2/#totalEnDoc2...],t2:...}
	termFrequency = {}
	for t in fij :
		termFrequency[t] = []
		i = 0
		for doc in fij[t] :
			if fdj[i] == 0 :
				termFrequency[t].append(0)
			else :
				termFrequency[t].append(doc/fdj[i])
			i += 1

	binaryTermOcurrence = {}
	# De la forma {t1 : [1 o  0 para Doc1,1 o 0 para Doc2...],t2:...}
	for t in fij :
		binaryTermOcurrence[t] = []
		for doc in fij[t] :
			if doc > 0 :
				binaryTermOcurrence[t].append(1)
			else :
				binaryTermOcurrence[t].append(0)

	tfidf = {}
	for t in termFrequency:
		tfidf[t] = []
		for doc in termFrequency[t]:
			# totalDocs es el numero total de documentos.
			# segun el paper es 1/fti[t], pero segun wikipedia es numero total
			# de documentos. con 1 da negativos.
			tfidf[t].append(doc*math.log(totalDocs/fti[t]))


	return termOcurrence,termFrequency,binaryTermOcurrence,tfidf
			

# Term occurrence: defines the absolute number of occurrences of a term.
# Term occurence = fij

# Term frequency:defines the relative frequency of a term in the document.
# Term frequency = fij /fdj

# Binary term occurrence: term occurrence is defined as the binary value.
# Binary Term Occurrence = 1 for fij>0 and = 0 otherwise.

# TF-IDF: it describes how important a word is for a document. It consists of two parts: term
# frequency (TF) and invert document frequency (IDF).
# TF-IDF= (fij /fdj)log(1/fti).