## Esercizio: build dell'immagine e run di un container per un'applicazione python

Si vuole creare una immagine Docker per poi mettere in esecuzione un container che lanci il codice contenuto in main.py.

Il codice in main.py stampa a console un numero float compreso tra
0 e 10.

I requisiti della nostra app (main.py) sono di avere bisogno di
python versione 3.10 e di avere installato numpy versione 1.26.4.

Step:
1. Scrivere il Dockerfile necessario per fare la build dell'immagine, facendo attenzione ai requisiti sopra.

2. Eseguire il comando per creare l'immagine del container (```docker build```).

3. Mettere in esecuzione il container. Quale numero ha estratto
il ```main.py```?

4. Fare push dell'immagine appena creata sul registry ufficale Docker Hub.

5. Inviarmi via mail (alessio.mora@unibo.it) il nome della vostra immagine docker dell'esercizio che posso trovare su Docker Hub (https://hub.docker.com/).