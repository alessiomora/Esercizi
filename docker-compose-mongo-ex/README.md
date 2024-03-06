## Esercizio docker compose: Applicazione Backend + DB

Si vuole creare containerizzare una applicazione che comprende un backend, che offre API RESTful, e un DB (MongoDB).

Informazioni:
* Il codice del backend si trova in app.py.
* Il codice del backend richiede python versione 3.6.
* Il codice del backend richiede le librerie python: flask versione 2.0.3
e pymongo versione 4.1.1.
* Flask permette la gestione e l'esposizione delle API RESTful del backend (eventualmente a dei frontend che lo chiamano, che esula da questo progetto).
* Pymongo mette a disposizione metodi python per interagire con un db mongo.
* Per il servizio DB, l'immagine ufficiale mongo:latest può fare al caso nostro.

Step 1. Scrivere il Dockerfile per il backend.
Step 2. Scrivere il docker-compose.yml. Domande: quanti servizi (services) avremo? (leggere anche dopo)

Step 2a. Scrivere lo scheletro del docker-compose.yml. Ogni servizio deve ovviamente prevedere una build o il caricamento di una base image ufficiale. Oltre a tali direttive, leggere di seguito e aggiungere.
Step 2b. Nel docker-compose, per il servizio backend, prevedere le seguenti direttive:
```
    ports:
      - "5000:5000"
    volumes:
      - .:/app
```
Step 2c. Il backend deve partire dopo che il db è up. Questo si definisce con una depends_on nel docker-compose.
```
    depends_on:
      - qui_inserire_il_nome_di_un_microservizio
```
Step 2d. Se si è previsto un servizio per il DB, inserire nei suoi attributi nel docker-compose.yml le seguenti entry:
```
    hostname: test_mongodb
    environment:
      - MONGO_INITDB_DATABASE=animal_db
      - MONGO_INITDB_ROOT_USERNAME=root
      - MONGO_INITDB_ROOT_PASSWORD=pass
    volumes:
      - ./init-db.js:/docker-entrypoint-initdb.d/init-db.js:ro
    ports:
      - 27017:27017
```
Step 3. Invocare il comando ```docker compose up```.

Step 4. Invocare il comando ```docker ps```. Quali container/servizi sono running?

Step 5. Tramite il browser visitare la pagina localhost:5000. Cosa succede? Chi sta rispondendo?

Step 6. Tramite il browser visitare la pagina localhost:5000/animals. Cosa succede? Chi sta rispondendo? Analizzare il file ```app.py```.

Step 7. Trovare il modo di aggiungere un nuovo animale alla lista di quelli visualizzati allo step precedente.
