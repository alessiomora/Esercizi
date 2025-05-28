# Usa l'immagine con JDK 21
FROM openjdk:21

WORKDIR /app

# Copia il file sorgente Java nel container
COPY Main.java .

# Compila Main.java
RUN javac Main.java

# Comando per eseguire l'app
CMD ["java", "Main"]