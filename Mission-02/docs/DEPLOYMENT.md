# Mission 02 — Deployment Guide

## Overview

This guide explains how to deploy the Mission 02 Python application using Docker and Kubernetes.

## Prerequisites

- Ubuntu Linux
- Docker
- kind
- kubectl
- Git

## 1. Verify the Environment

```bash
docker --version
kind --version
kubectl version --client
```

## 2. Build the Docker Image

From the Mission-02 directory:

```bash
docker build -t mission02-web:v1 application/
```

Verify:

```bash
docker images mission02-web
```

## 3. Create the Kubernetes Cluster

```bash
kind create cluster \
  --name mission02 \
  --config kubernetes/kind-config.yaml \
  --wait 180s
```

Verify:

```bash
kubectl get nodes
```

## 4. Load the Docker Image

```bash
kind load docker-image mission02-web:v1 --name mission02
```

## 5. Deploy the Application

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

Verify:

```bash
kubectl rollout status deployment/mission02-web
kubectl get deployments
kubectl get pods -o wide
kubectl get services
```

## 6. Test the Application

In the first terminal:

```bash
kubectl port-forward service/mission02-web 18081:80
```

In a second terminal:

```bash
curl http://127.0.0.1:18081/
curl http://127.0.0.1:18081/health
```

Expected health response:

```json
{"status": "healthy"}
```

## 7. Scale the Application

```bash
kubectl scale deployment mission02-web --replicas=3
kubectl get pods -l app=mission02-web
```

Restore two replicas:

```bash
kubectl scale deployment mission02-web --replicas=2
```

## 8. Build Version 2

```bash
docker build \
  -t mission02-web:v2 \
  -f application/Dockerfile.v2 \
  application/

kind load docker-image mission02-web:v2 --name mission02
```

## 9. Perform a Rolling Update

```bash
kubectl set image deployment/mission02-web web=mission02-web:v2
kubectl set env deployment/mission02-web APP_VERSION=2.0
kubectl rollout status deployment/mission02-web
```

Verify the application endpoints before rollback.

## 10. Restore Version 1

```bash
kubectl set image deployment/mission02-web web=mission02-web:v1
kubectl set env deployment/mission02-web APP_VERSION=1.0
kubectl rollout status deployment/mission02-web
```

Verify that the application returns version 1.0.

## 11. Review Deployment History

```bash
kubectl rollout history deployment/mission02-web
```

Inspect an available revision using its actual revision number.

## Conclusion

This lab demonstrates Docker image management, Kubernetes deployments, service networking, scaling, health monitoring, and application rollback.
