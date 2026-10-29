# Validation Evidence — Mission 01

Evidence transcribed from successful lab command output.

## Terraform and S3
- Terraform: `Apply complete! Resources: 2 added, 0 changed, 0 destroyed.`
- Resources: `aws_s3_bucket.mission01`, `aws_s3_bucket_public_access_block.mission01`
- Bucket: `multicloud-mission01-lab`
- LocalStack health: HTTP 200; `s3` service `available` on Community 3.8.1.
- AWS CLI version: `aws-cli/2.39.1`
- Original and retrieved file SHA-256:
  `be73876eb6b070adc5dac3f4d9eb39d4c28d5eb2c99c795071f5dfcba42134a3`

## MySQL
- Container: MySQL 8.4, healthy.
- Database: `mission01db`; 2 records in `cloud_resources`.
- Backup: exit code 0; `mysqldump --no-tablespaces --single-transaction --quick`.
- Backup file SHA-256:
  `a272f323272ed3b9c56415ed9b66ddbea09926f463456d4769b6832137bd1b56`
- Restore target: `mission01_restore_test`; exit code 0; 2 restored records.
- Original/restored query results SHA-256 (matching):
  `a2350aac9f1c6fba7f8ad88d87d39fbac2e185ba274f99b4b1376e80fd218438`

These hashes establish integrity of the tested files and query results. They are not a substitute for full backup verification of all possible data types or production recovery testing.
