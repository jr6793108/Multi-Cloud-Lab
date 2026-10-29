# Mission 02 — Kubernetes Troubleshooting Guide

## Overview

This guide documents troubleshooting procedures for the Docker and Kubernetes environment used in Mission 02.

## 1. Verify Cluster Health

Check the Kubernetes nodes:

```bash
kubectl get nodes -o wide
```

Check system pods:

```bash
kubectl get pods -A
```

Expected result: the Kubernetes node is Ready and the system pods are running.

## 2. Troubleshoot Application Pods

List application pods:

```bash
kubectl get pods -l app=mission02-web -o wide
```

Inspect a specific pod:

```bash
kubectl describe pod POD_NAME
```

View application logs:

```bash
kubectl logs POD_NAME
```

Replace POD_NAME with an actual pod name from the output.

Common problems include container crashes, missing images, insufficient resources, and failed health probes.

## 3. Troubleshoot ImagePullBackOff

Check available Docker images:

```bash
docker images mission02-web
```

Load the application image into kind:

```bash
kind load docker-image mission02-web:v1 --name mission02
```

Verify that the image name and tag match the Kubernetes Deployment configuration.

## 4. Troubleshoot Deployment Readiness

```bash
kubectl get deployments
kubectl describe deployment mission02-web
kubectl get events --sort-by=.metadata.creationTimestamp
```

Check readiness probes, resource limits, image availability, and pod events.

## 5. Troubleshoot Kubernetes Services

List Services:

```bash
kubectl get services
```

Check Service endpoints:

```bash
kubectl get endpointslices \
  -l kubernetes.io/service-name=mission02-web
```

Confirm that the Service selector matches the application pod labels.

## 6. Troubleshoot Port Forwarding

Start port forwarding:

```bash
kubectl port-forward service/mission02-web 18081:80
```

Keep that terminal open.

From another terminal:

```bash
curl -v http://127.0.0.1:18081/health
```

If the connection fails, check whether port forwarding is still running and whether the application pods are Ready.

## 7. Troubleshoot Scaling

Check the desired and available replicas:

```bash
kubectl get deployment mission02-web
```

Inspect application pods:

```bash
kubectl get pods -l app=mission02-web
```

Check recent events:

```bash
kubectl get events --sort-by=.metadata.creationTimestamp
```

## 8. Review Rolling Updates

Display the rollout history:

```bash
kubectl rollout history deployment/mission02-web
```

Inspect an available revision, for example:

```bash
kubectl rollout history deployment/mission02-web --revision=7
```

Revision numbers may differ in another cluster.

## 9. Restore a Known-Good Version

First identify the revision containing the desired application image and environment settings.

Then run, substituting the correct revision number:

```bash
kubectl rollout undo deployment/mission02-web --to-revision=7
```

Wait for the rollout:

```bash
kubectl rollout status deployment/mission02-web
```

Verify the application version and health endpoint.

## 10. Common Terminal Mistakes

### Incomplete Shell Commands

A `>` prompt can indicate that Bash is waiting for an unfinished quotation or heredoc.

Press Ctrl+C to cancel the incomplete command.

### Copying Expected Output as Commands

Text such as `mission02-web:v1` is an image identifier, not an executable command.

### Revision Placeholders

The `--revision` and `--to-revision` flags require actual numeric revision values, not the literal word REVISION.

## Conclusion

These procedures provide a repeatable approach to troubleshooting Kubernetes workloads, networking, container images, deployment health, and application recovery.
