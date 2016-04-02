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


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn import cross_validation
from featureSelectionNuevo import obtainFeatures
import numpy as np
import re
import sys
from sklearn.naive_bayes import MultinomialNB

def leerTuits(ids):
	tuits = []
	for i in range(1,len(ids)):
		f = open("./CleanUserDocs/"+str(i)+".txt")
		tuits.append(f.read())
	f.close()
	return tuits

def leerStop(fileSW):
  f = open(fileSW,'r')
  stop_words = f.read().splitlines()
  f.close()
  return stop_words

def extraerTopicos(modelo, feature_names, n_top_words):
	topicos = []
	for topic_idx, topic in enumerate(modelo.components_):
		nombres = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
		topicos.append(nombres)
	return topicos

def main(numTop,n_pal):

	n_features = 3640
	n_topics = numTop
	n_top_words = n_pal

	f = open('./dataSet.dat','r')
	datos = [] 						# Arreglo con id del usuario y clasificación 
	for i in range(0,2000):
		linea = f.readline()
		datos.append(linea.split())
	f.close()

	# Separación del conjunto de prueba del de entrenamiento (70% entrenamiento - 30% prueba)
	dataTrain, dataTest = cross_validation.train_test_split(datos,test_size=0.3)

	tuits = leerTuits(dataTrain)
	stop_words = leerStop('stopWords.txt')

	#Sacando tf features para LDA
	tf_vectorizer = CountVectorizer(max_df=0.95, min_df=0.2, 
									max_features=n_features,
									stop_words=stop_words,
									strip_accents="ascii")
	tf = tf_vectorizer.fit_transform(tuits)

	#Entrenando el modelo LDA con tf features, n_topics y 70% de los datos
	lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=5,
	                                learning_method='online',
	                                learning_offset=50.,
	                                random_state=0)
	lda.fit(tf)

	#Tópicos en el modelo LDA
	tf_feature_names = tf_vectorizer.get_feature_names()
	topicos = extraerTopicos(lda, tf_feature_names, n_top_words)

	docs = []
	for d in datos :
		docs.append(int(d[0]))

	termOcurrence,termFrequency,binaryTermOcurrence,tfidf = obtainFeatures(topicos,docs)
	aux = [termOcurrence,termFrequency,binaryTermOcurrence,tfidf]

	i = 0
	topics = []
	for t in topicos : 
		topics.append(i)
		i += 1

	# Matriz :
	# [[termOcT1,termFreqT1,binTermOcT1,tfidfT1,termOcT2...]]
	mTrainFeatures = []
	for i in range(0,len(dataTrain)):
		mTrainFeatures.append([])

	for t in topics :
		for f in aux :
			for i in range(0,len(dataTrain)):
				mTrainFeatures[i].append(f[t][int(dataTrain[i][0])-1])

	# Creando la matriz de features de numpy de entrenamiento
	npTrainFeatures = np.array(mTrainFeatures,dtype=float)


	# Matriz de features para pruebas
	mTestFeatures = []
	for i in range(0,len(dataTest)):
		mTestFeatures.append([])

	for t in topics :
		for f in aux :
			for i in range(0,len(dataTest)):
				mTestFeatures[i].append(f[t][int(dataTest[i][0])-1])

	npTestFeatures = np.array(mTestFeatures,dtype=float)

	# Targets de entrenamiento.
	trainTargets = []
	for elem in dataTrain :
		trainTargets.append(elem[1])

	# Creando el arreglo de train targets de numpy.
	npTrainTarget = np.array(trainTargets)

	# Targets de prueba.
	testTargets = []
	for elem in dataTest :
		testTargets.append(elem[1])

	# Creando el arreglo de test targets de numpy
	npTestTarget = np.array(testTargets)

	# Creando el Gaussian Naive Bayes
	mnb = MultinomialNB(alpha=0.01)
	y_pred = mnb.fit(npTrainFeatures,npTrainTarget).predict(npTestFeatures)

	tp, tn, fp, fn = 0, 0, 0, 0
	for i in range(len(testTargets)):
		if (npTestTarget[i] == y_pred[i]):
			if (npTestTarget[i]=="1"):
				tp += 1
			else:
				tn +=1
		else:
			if (npTestTarget[i]=="1"):
				fp += 1
			else:
				fn +=1

	return [tp,fn,fp,tn], topicos

# Programa principal
if __name__ == "__main__":
	exactitud,tp,fn,fp,tn = 0,0,0,0,0 
	t = int(sys.argv[1])
	p = int(sys.argv[2])
	print("Ejecución con T = ",t)
	print("Palabras por tópico = ",p)
	for i in range(0,10):
		res,topicos = main(t,p)
		tp += res[0]
		fn += res[1]
		fp += res[2]
		tn += res[3]
	exactitud = (tp/10 + tn/10)/600
	print("Exactitud: ",exactitud)
	print("Matriz de confusión:")
	print(str(tp/10) + " " + str(fn/10) + "\n" + str(fp/10) + " " + str(tn/10) + "\n")
	print("Tópicos:")
	print(topicos)