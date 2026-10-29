# Mission 02 — Lessons Learned

## Overview

Mission 02 provided hands-on experience deploying and managing a containerized application using Docker and Kubernetes.

## 1. Containerization

Built a Python HTTP application and packaged it into Docker images.

Learned how Dockerfiles, image tags, and container images support application deployment.

## 2. Kubernetes Administration

Created a local Kubernetes cluster using kind.

Practiced managing Kubernetes nodes, Deployments, pods, and Services using kubectl.

## 3. Application Networking

Configured a ClusterIP Service and used port forwarding to verify application connectivity.

## 4. Health Monitoring

Configured HTTP readiness and liveness probes.

Learned how Kubernetes uses health checks to determine application readiness and restart unhealthy containers.

## 5. Scaling and Self-Healing

Scaled the application from two to three replicas.

Observed Kubernetes replace a deleted pod and restore the desired replica count.

## 6. Rolling Updates

Created a second application image and inspected Kubernetes Deployment revision history.

Learned how image and environment variable changes affect Deployment revisions.

## 7. Rollback and Recovery

Restored the original application image and environment configuration.

Verified that the application returned version 1.0 and passed its health check.

## 8. Troubleshooting

Practiced:
- Inspecting pod status and events
- Reviewing Deployment history
- Checking Service endpoints
- Testing application connectivity
- Resolving terminal command errors

## 9. Future Improvements

- Complete version 2 HTTP validation
- Add automated application testing
- Introduce GitHub Actions CI/CD
- Implement centralized monitoring and logging
- Expand the lab to multiple Kubernetes nodes

## Conclusion

Mission 02 strengthened practical skills in containerization, Kubernetes operations, application availability, troubleshooting, and recovery.
