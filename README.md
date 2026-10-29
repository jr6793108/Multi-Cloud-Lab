# Multi-Cloud Infrastructure Engineering Lab

A hands-on infrastructure engineering portfolio focused on
Terraform, AWS, Google Cloud, Docker, Kubernetes,
database administration, and cloud migration.

## Project Objectives

- Build reproducible infrastructure using Terraform.
- Deploy and manage cloud-compatible storage.
- Configure containerized relational databases.
- Practice backup, restoration, and integrity validation.
- Progress from local simulation to real cloud deployments.
- Document troubleshooting and operational procedures.

## Lab Missions

| Mission | Description | Status |
|---------|-------------|--------|
| Mission 01 | Terraform, S3-compatible storage, and MySQL | Local lab completed |
| Mission 02 | Containers and Kubernetes | Planned |
| Mission 03 | Cloud data migration | Planned |

## Mission 01 — Completed Work

- Configured Ubuntu 24.04 on VMware.
- Installed Terraform and Docker.
- Deployed LocalStack 3.8.1 for S3 emulation.
- Provisioned an S3-compatible bucket using Terraform.
- Verified file upload and retrieval using SHA-256.
- Deployed MySQL 8.4 using Docker Compose.
- Created and populated a relational database.
- Generated a MySQL logical backup.
- Restored the backup into a separate database.
- Verified matching original and restored records.

[View Mission 01](Mission-01/README.md)

## Technologies

Terraform | Docker | Linux | AWS CLI | LocalStack |
MySQL | Git | GitHub

## Cloud Deployment Status

The completed exercises currently use local cloud
emulation and containerized services.

Real AWS and Google Cloud deployments are future phases.

## Security

Credentials, Terraform state, runtime data, and database
backups are excluded from version control.
