# shustr-restapi
shustr (Shuffle String) Simple Restful Api to Jumble a string.

Documentation

What does this code do:

It is a Rest API, that Jumbles (randomizes the order of the characters) a string and also reports back the last 10 calls, example



Usage:

A - From an alternate ssh terminal (separate from the session that is not running the flask server) using curl

To jumble a string (the string in this case is "test"):

curl "http://127.0.0.1:5000/Jumble/test"

(and you will get a string such as "stet", results may vary as it is a random order)

To get the last 10 operations:

curl "http://127.0.0.1:5000/Audit"


B - From a browser pointing to the instance on your network 

To jumble a string:

http://127.0.0.1:5000/Jumble/test

(the result will be shown on the browser)

To get the last 10 operations, point the browser to:

http://127.0.0.1:5000/Audit



For this project, I am providing instructions on


* How to test the API on your machine
* how to containerize it with Docker
* how to deploy/run it in Minikube 


Prerequisites:
In order to run the code, I created an Ubuntu 22.04 vm and installed pip (get the flask libraries),
 if you would like to fun the solution on Minikube you might consider provisioning a vm with at least:

* two processor cores
* 3 GB RAM
* 40 GB Hard disk space.   

Once you have this vm running clone the repo, the Readme.md files is the one that contains this documentation 

The flask-restful libraries are needed on your virtual environment for this project to run, you can install it with:

pip3 install flask-restful


1. how to run the code locally on your machine, just run 

python3 app.py

a similar message to the one above will show up:

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ###-###-###

On a second terminal window (using curl) or on a browser pointing to the external IP of your Virtual machine, you can start sending requests to the running server.
 

2. Containerizing the API  (you will need docker installed, if you need it follow the instruction on: https://docs.docker.com/engine/install/ubuntu/  ) 

Build
I provided a Dockerfile to Build a docker image you may use the same file and you may create your own docker image witht the command:

docker build -t shustr .

And to run container
docker run -d -p 5000:5000 --name python-restapi shustr  

The docker image for the solution can be also accessed at:  https://hub.docker.com/repository/docker/giochajon/shustr-restapi


3. Running in Minikube

I have also provided a pod.yml  and a deployment.yml file so the solution can be run on minikube

3.1 start Minikube with the command
minikube start

3.2 because you need to use kubectl run the following:
minikube kubectl -- get pods -A

3.3 to invoke the creation of the pod with the api use 
 minikube kubectl -- create -f pod.yml

3.3.1 Optionally remember to add the alias to make the Minikube commands shorter: 
alias kubectl="minikube kubectl --"

3.4  Deploying:
kubectl create -f deployment.yml

3.5 to allow access with services I added the service.yml file 

kubectl create -f service.yml

3.6 get the ip address of the service to access it though the browser (on the vm) with:

kubectl cluster-info

or 
minikube service shustr-restapi  

to get the address to where you can curl to.
