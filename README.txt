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

Se necesitan tener las siguientes librerías instaladas antes de correr el proyecto:
	- Numpy
	- Scipy
	- Scikit-learn
	- Re
	- Tweepy (solo en caso que quieran obtenerse nuevos usuarios)

Lo necesario para correr el proyecto es:
	-> clasificador.py : aquí se encuentra todo lo relacionado al clasificador y los tópicos
	-> featureSelectionNuevo.py : en este archivo está todo lo relacionado a los cálculos de las frecuencias
								  de cada tópico en los documentos.
	-> dataSet.dat : archivo con la identificación de cada usuario y su respectiva clasificación (conjunto de prueba y de entrenamiento)
	-> Fichero CleanUserDocs : aquí se encuentran todos los archivos de cada usuario con sus respectivos tuits.
	-> stopWords.txt : archivo que contiene la lista de palabras vacías utilizadas para la extracción de los tópicos.

Para correr el proyecto debe realizarse el comando python3 clasificador.py numeroTopicos numPalabras
donde numeroTopicos y numPalabras son enteros que representan la cantidad de tópicos que desea utilizarse y la cantidad de palabras
deseadas por cada tópico, respectivamente.