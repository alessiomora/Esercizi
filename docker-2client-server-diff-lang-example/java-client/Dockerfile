FROM openjdk:21

WORKDIR /app

COPY . .

# Scarica la libreria org.json in modo semplice
RUN curl -L -o json.jar https://repo1.maven.org/maven2/org/json/json/20240303/json-20240303.jar

# Compila
RUN javac -cp json.jar Main.java

# Esegui
CMD ["java", "-cp", ".:json.jar", "Main"]
