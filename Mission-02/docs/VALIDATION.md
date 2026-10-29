# Mission 02 — Kubernetes Validation Report

## Project Overview

This report documents the Docker and Kubernetes operational tests completed during Mission 02.

Environment:
- Ubuntu Linux virtual machine
- Docker container engine
- kind single-node Kubernetes cluster
- Python HTTP application
- Kubernetes Deployment: mission02-web
- Kubernetes Service: mission02-web

## 1. Docker Image Validation

Two application images were successfully built:

- mission02-web:v1
- mission02-web:v2

Both images were available in the local Docker environment.

Result: PASSED

## 2. Kubernetes Deployment

The application was deployed using Kubernetes manifests.

Verified:
- Deployment available
- Two application replicas ready
- Application pods running
- No pod restarts in the final verification

Result: PASSED

## 3. Service Networking

A ClusterIP Service was configured.

The Service EndpointSlice successfully identified the application pods.

The application was accessed using kubectl port-forward.

Result: PASSED

## 4. Scaling Test

The Deployment was scaled from two to three replicas.

Verified:
- Desired replicas: 3
- Ready replicas: 3
- Service endpoints: 3

Result: PASSED

## 5. Self-Healing Test

A managed application pod was deleted.

Kubernetes created replacement pods to maintain the desired replica count.

Result: PASSED

## 6. Rolling Update

Kubernetes revision 6 recorded:

- Image: mission02-web:v2
- APP_VERSION: 2.0

The configuration change was recorded successfully.

Version 2 HTTP responses have not yet been captured.

Result: CONFIGURATION VERIFIED; HTTP TEST PENDING

## 7. Rollback Test

Kubernetes revision 7 restored:

- Image: mission02-web:v1
- APP_VERSION: 1.0

The Deployment returned to two ready replicas.

Application response confirmed:
- Version: 1.0
- Status: running

Health endpoint returned:

```json
{"status": "healthy"}
```

Result: PASSED

## 8. Evidence

The evidence directory contains:

- deployment-v2.txt
- pods-v2.txt
- deployment-final.txt
- pods-final.txt
- rollout-history-final.txt

## 9. Final Assessment

Mission 02 demonstrates:

- Docker containerization
- Kubernetes deployment management
- Service networking
- Application scaling
- Pod recovery
- Deployment revision management
- Rollback and health verification

Outstanding item: Capture a successful version 2 HTTP response.
