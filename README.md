# Mission 01 — Local Multi-Cloud Infrastructure Lab

## Overview
This project demonstrates local infrastructure provisioning and recovery workflows as preparation for AWS S3 and Google Cloud SQL exercises. **No live AWS or Google Cloud resources were deployed during these phases.**

## Architecture
- Ubuntu 24.04 VMware virtual machine
- Terraform with AWS provider targeting a localhost LocalStack S3 endpoint
- LocalStack Community 3.8.1, bound to `127.0.0.1:4566`
- MySQL 8.4 LTS in Docker, bound to `127.0.0.1:3306`
- Persistent MySQL Docker volume

## Verified results
| Test | Evidence |
|---|---|
| Terraform apply | 2 resources added, 0 changed, 0 destroyed |
| S3 bucket | `multicloud-mission01-lab` |
| S3 upload/download | Original and downloaded files have identical SHA-256 digests |
| MySQL connection | `labuser` authenticated to `mission01db` |
| MySQL backup | `mysqldump --no-tablespaces --single-transaction --quick` completed with exit code 0 |
| Restore | `mission01_restore_test` restored with exit code 0; 2 records |
| Data comparison | Original and restored query results have identical SHA-256 digests |

See [validation evidence](docs/VALIDATION.md), [architecture](docs/ARCHITECTURE.md), and [troubleshooting](docs/TROUBLESHOOTING.md).

## Reproducing
1. Install Docker, Terraform, and AWS CLI on an isolated Linux lab VM.
2. Configure LocalStack S3 using a pinned, tested image and loopback-only port mapping.
3. Use Terraform with its AWS S3 endpoint set to `http://127.0.0.1:4566` and **dummy** credentials. Review `terraform plan` before applying.
4. Deploy MySQL 8.4 with Docker Compose, using credentials in an untracked `.env` file and a persistent volume.
5. Test the database, create a logical backup, restore to a separate database, and compare results.

**Security:** Do not commit `.env`, Terraform state, local storage, or SQL backup files. Do not expose the lab services publicly. Older LocalStack images are for isolated training only.

## Next steps
- Publish sanitized Terraform and Docker Compose configurations.
- Prepare budget alerts and least-privilege credentials before any real cloud deployment.
- Deploy real AWS S3 and Google Cloud SQL resources in later exercises.
