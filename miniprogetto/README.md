# Mini-progetto di ASD 2014/2015

Pagina originale: http://didawiki.cli.di.unipi.it/doku.php/matematica/asd/asd_14/mini_progetto_14

Il progetto si basa su dati presi dal mondo reale e prevede di elaborare un insieme S di alcune pagine prese da wikipedia e “ripulite” dalla formattazione: wiki-small.zip (ringraziamenti a Marco Cornolti e Francesco Piccinno per aver messo a disposizione tali dati).

Lo scopo è costruire un grafo G=(V,E) a partire dall'insieme S, dove V rappresenta le parole distinte che si trovano nelle varie pagine in S e un arco (u,v) di E rappresenta il fatto che le due parole u e v appaiono consecutivamente (in alternativa, sufficientemente vicine) in una di tali pagine. È lasciata allo studente la scelta se ignorare le “stop word” come articoli, preposizioni, ecc.

Utilizzando la struttura di tale grafo G, il progetto richiede allo studente di concepire e implementare algoritmi per stampare le triplette di parole che formano dei triangoli (cioè la clique K_3) in G. 
