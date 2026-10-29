# Mission 02 — Docker and Kubernetes Operations

## Project Overview

This project demonstrates containerization and Kubernetes administration using Python, Docker, kind, and kubectl.

## Objectives

- Build a Python web application
- Containerize the application with Docker
- Deploy a Kubernetes cluster using kind
- Configure Deployments and Services
- Implement readiness and liveness probes
- Scale application replicas
- Demonstrate Kubernetes self-healing
- Practice rolling updates and rollback
- Document operational troubleshooting

## Technologies

- Ubuntu Linux
- Python 3.12
- Docker
- Kubernetes
- kind
- kubectl
- Git and GitHub

## Architecture

Ubuntu VM
  → Docker Engine
  → kind Kubernetes Cluster
  → Kubernetes Deployment
  → Python Application Pods
  → ClusterIP Service

## Completed Exercises

1. Docker application deployment
2. Kubernetes cluster installation
3. Deployment and Service configuration
4. Scaling from two to three replicas
5. Pod deletion and automatic replacement
6. Version 2 Deployment configuration
7. Restoration of version 1
8. HTTP health verification

## Validation Results

- Final Deployment: 2/2 replicas ready
- Application version: 1.0
- Application status: running
- Health endpoint: healthy
- Version 2 Deployment revision recorded
- Version 2 HTTP validation remains outstanding

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [Validation](docs/VALIDATION.md)
- [Lessons Learned](docs/LESSONS-LEARNED.md)

## Project Status

Kubernetes deployment, scaling, self-healing, and rollback verification completed.
