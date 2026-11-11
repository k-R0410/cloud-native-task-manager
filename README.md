# Cloud Native Task Manager

A Flask-based REST API deployed using Docker and Kubernetes.

## Technologies
- Python and Flask
- Docker
- Kubernetes (Minikube)
- Git and GitHub

## Features
- Create tasks
- View all tasks
- Update task completion status
- Delete tasks
- Health check endpoint
- Kubernetes deployment with multiple replicas
- Rolling updates and rollback

## Run locally

Install dependencies:

pip install -r app/requirements.txt

Run the application:

python app/app.py

## Docker

Build the image:

docker build -f docker/Dockerfile -t cloud-native-task-manager:v1 .

## Kubernetes

Apply the deployment:

kubectl apply -f kubernetes/
