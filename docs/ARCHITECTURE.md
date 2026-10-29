# Architecture — Mission 01

```text
VMware Ubuntu 24.04 VM
|
+-- Terraform (local AWS provider endpoint)
|   +-- LocalStack Community 3.8.1 (127.0.0.1:4566)
|       +-- S3 bucket: multicloud-mission01-lab
|
+-- Docker Compose
    +-- MySQL 8.4 (127.0.0.1:3306)
        +-- Persistent Docker volume
        +-- mission01db
        +-- mission01_restore_test
```

The S3 bucket is provisioned by Terraform through LocalStack's local AWS-compatible API. MySQL is independently deployed by Docker Compose. The database restore is a local disaster-recovery rehearsal, not a Google Cloud SQL migration.

## Boundaries
- Loopback-bound ports are accessible on the Ubuntu VM, not directly exposed to the LAN.
- LocalStack 3.8.1 is an older image; use only in an isolated training environment.
- No production or real cloud credentials belong in this repository.
