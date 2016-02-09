#  Il progetto si basa su dati presi dal mondo reale e prevede di
#  elaborare un insieme S di alcune pagine prese da wikipedia e
#  “ripulite” dalla formattazione: wiki-small.zip (ringraziamenti a
#  Marco Cornolti e Francesco Piccinno per aver messo a disposizione
#  tali dati).

# Lo scopo è costruire un grafo G=(V,E) a partire dall'insieme S, dove
# V rappresenta le parole distinte che si trovano nelle varie pagine
# in S e un arco (u,v) di E rappresenta il fatto che le due parole u e
# v appaiono consecutivamente (in alternativa, sufficientemente
# vicine) in una di tali pagine. È lasciata allo studente la scelta se
# ignorare le “stop word” come articoli, preposizioni, ecc.

 # Utilizzando la struttura di tale grafo G, il progetto richiede allo
 # studente di concepire e implementare algoritmi per stampare le
 # triplette di parole che formano dei triangoli (cioè la clique K_3)
 # in G.

import os, re, pickle

percorso = 'wiki-small'
testo = '15641.txt'
stopwordsfile = 'stopwords_en.txt'

# Creo un grafo con un dizionario che associa ogni parola a un
# elemento della classe vertice. Salvo le parole anche in una lista,
# che può essere più semplice da gestire per eseguire un
# ordinamento. I triangoli verranno invece salvati nella lista cliques
stopwords = {}
diz = {}
vertici = []
cliques = []

# Ogni vertice contiene una parola e registra la parola, il suo numero
# di occorrenze, la lista di adiacenza e un indice che può essere
# utile nella ricerca dei triangoli
class Vertice:
    def __init__(self,id,occ):
        self.id = id
        self.occ = occ
        self.adj = []
        self.index = 0

# Carico le stopwords: l'elenco che ho scelto contiene 571 parole ed è
# una leggera modifica di quello utilizzato da MySQL
def loadStopwords(stopwordsfile):
    with open(stopwordsfile,'r') as swf:
        for line in swf:
            split0=re.split('[\s]',line)
            for sw in split0:
                if sw:
                    stopwords[sw]=True
    print('Ho caricato le stopwords.')

# Considero la possibilità di salvare dati, come il dizionario e la
# lista dei vertici o i triangoli trovati, in file pickle per
# richiamarli velocemente in caso di necessità
def saveDataPickle(data,filename):
    with open(filename, "wb") as output_file:
        pickle.dump(data, output_file)

def loadDataPickle(filename):
    with open(filename, "rb") as input_file:
        data = pickle.load(input_file)
        return data

# Carico tutti i file in una cartella
def loadDir(mypath):
    for myfile in os.listdir(mypath):
        print("carico %s" %(myfile))
        loadFile(mypath, myfile)

# Carico tutte le parole in un file: una parola la definisco tale se
# separata da caratteri non ASCII. Escludo le parole di lunghezza uno
# e le stopwords e uniformo le parole rendendo tutti i caratteri
# minuscoli. Per ogni parola trovata creo un vertice e lo aggiungo al
# dizionario. Aggiungo la parola alla lista di adiacenza della parola
# precedente e la parola precedente alla lista di adiacenza della
# parola che sto considerando ora.
def loadFile(mypath, myfile):
    with open(os.path.join(mypath, myfile),'r') as f:
        for line in f:
            split1 = re.split('[^a-zA-Z0-9]',line)        
            prec = False
            for word in split1:
                word = word.lower()
                if (word not in stopwords) and (len(word)>1):
                    if word not in diz:
                        diz[word] = Vertice(word,1)
                        vertici.append(word)
                    else:
                        diz[word].occ += 1
                    if prec and word!=prec: 
                        if word not in diz[prec].adj:
                            diz[prec].adj.append(word)
                        if prec not in diz[word].adj:
                            diz[word].adj.append(prec)
                    prec=word

# Prima ordino la lista di vertici in base alle occorrenze delle
# parole rappresentate, dalla più frequente alla meno. Per trovare i
# triangoli scandisco tutti gli archi (s,t) e comparo le liste di
# adiacenza di s e t. Invece di scandirle tutte, creo un dizionario
# con liste dinamiche che riempio mano a mano per diminuire il tempo
# di scorrimento delle liste. Quando trovo una triangolo lo aggiungo a
# una lista a parte.
def findCliques():
    print('inizio a cercare i triangoli')
    print('sorting')
    vertici.sort(key = lambda x: diz[x].occ, reverse = True)
    print('ho finito il sorting')
    A = {}
    for i in range(len(vertici)):
        A[vertici[i]] = set()
        diz[vertici[i]].index = i
    total = len(vertici)
    counter = 0
    for s in vertici:
        counter += 1
        for t in diz[s].adj:
            if diz[s].index < diz[t].index:
                for v in A[s].intersection(A[t]):
                    triangolo = [s,t,v]
                    # triangolo.sort(key = lambda x: diz[x].occ, reverse = True)
                    cliques.append(triangolo)
                A[t].add(s)
        if counter % 100 == 0:
            print("vertice %d di %d" %(counter,total))

# Mettendoci molto tempo, posso trovare le cliques con le parole la
# somma delle cui occorrenze è massima
def orderCliques():
    cliques.sort(key = lambda x: (diz[x[0]].occ+diz[x[1]].occ+diz[x[2]].occ), reverse = True)


# Se ho già salvato il dizionario e la lista dei vertici lo posso
# ricaricare.
def eseguiSalvato():
    global diz, vertici
    loadStopwords(stopwordsfile)
    diz = loadDataPickle('data/diz.pickle')
    vertici = loadDataPickle('data/vertici.pickle')
    findCliques()
    print('ho trovato tutti i triangoli: %d' %len(cliques))
    orderCliques()
    saveDataPickle(cliques,'data/cliques.pickle')
    print('ho salvato i dati')
    [ print(cliques[i]) for i in range(0,20) ]

def eseguiCompleto():
    loadStopwords(stopwordsfile)
    loadDir(percorso)
    saveDataPickle(diz,'data/diz.pickle')
    saveDataPickle(vertici,'data/vertici.pickle')
    findCliques()
    print('ho trovato tutti i triangoli: %d' %len(cliques))
    orderCliques()
    saveDataPickle(cliques,'data/cliques.pickle')
    print('ho salvato i dati')
    [ print(cliques[i]) for i in range(0,20) ]

# Scandisco un solo file per provare
def eseguiProva():
    loadStopwords(stopwordsfile)
    loadFile(percorso,testo)
    findCliques()
    orderCliques()
    [ print(i) for i in cliques ]

# eseguiProva()
# eseguiSalvato()
eseguiCompleto()
