## Example Kubernetes 

1. Create a new project
```npm init -y```
2. Install the dependencies
```npm i express```
3. Create a new file called index.js

Let's create a simple Express server that listens on port 3000 and returns a response.
```
//simple express server
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Example app listening on port 3000!');
});
```
Run this by typing:
```
node index.js
```


Now it's time to Dockerize our application.

Dockerfile
docker-compose.yml

Nice! Now it's the turn of Kubernetes.

Kubernetes

Before we start, be sure Kubernetes is enabled in Docker Desktop.

We will keep it as minimal as possible by creating a deployment and a service.

Just three definitions to get started as soon as possible.

pod: the smallest deployable unit of computing that can be created and managed in Kubernetes.

deployment: a Kubernetes object that manages a set of pods. It is responsible for creating and updating pods.

service: an abstraction that defines a logical set of pods and a policy by which to access them. They are used to expose a set of pods to external traffic.

Create the deployment

We will create a deployment in less than 20 lines of code.

At the root of the project, create a new file called deployment.yaml and add the following:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: myapp
          image: myapp:1.0
          ports:
            - containerPort: 3000
```

Explanation of the ```deployment.yaml``` file:

apiVersion: apps/v1 - the version of the Kubernetes API

kind: Deployment - the kind of object we want to create. In this case, a deployment.

name: myapp - the name of the deployment

replicas: 3 - the number of replicas of the deployment

image: myapp:1.0 - the image of the container. We defined this in the docker-compose.yml file

ports: - the ports of the container. 3000 in this case.

Before we create the deployment, let's check if there are any deployments in the cluster:
```kubectl get deployments```

Let's create the deployment by typing: 
```kubectl apply -f deployment.yaml```

Then let's try to get the deployments again:

```kubectl get deployments```

We can also get a detail of the pods:
```kubectl get pods```

But creating a deployment is not enough. We need to expose the deployment to the outside world!

Create the service
We will create a service in 11 lines of code.

At the root of the project, create a new file called service.yaml and add the following:
```
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 3000
  type: LoadBalancer
```

This is enough to expose the deployment to the outside world (port 80)

Before we apply this configuration, let's check if there are any services in the cluster:
```kubectl get services```

There is one called Kubernetes but that's the default service that is created when you install Kubernetes.

Let's create the service by typing:

```kubectl apply -f service.yaml```
Then let's try to get the services again:
```kubectl get services```

Finally, visit localhost:80 in your browser and you should see Hello Kubernetes!

Clean up

To clean up, delete the deployment and the service:
```kubectl delete -f deployment.yaml```
```kubectl delete -f service.yaml```