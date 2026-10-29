# Troubleshooting Lessons

## MinIO image pulls failed
The tested Quay image returned HTTP 401; the tested Docker Hub repository was unavailable. The lab switched to LocalStack.

## LocalStack stable required activation
LocalStack 2026.10.4 exited with license activation error (exit code 55). A pinned legacy Community image, `localstack/localstack:3.8.1`, started successfully with S3 available. The old image should only be used in an isolated lab.

## AWS CLI package unavailable
`sudo apt install awscli` had no installation candidate on the VM. AWS CLI v2 was installed using the official Linux distribution; version 2.39.1 was verified.

## MySQL login denied
Manual password entry produced `ERROR 1045`. Using the container's configured `MYSQL_PASSWORD` environment variable succeeded. No password reset was needed.

## mysqldump PROCESS privilege error
The first dump attempted to read tablespace metadata without PROCESS privileges. Adding `--no-tablespaces` yielded a successful backup without granting broad additional privileges.

## Backup validation
A successful dump exit code and SQL content inspection were followed by restoration into `mission01_restore_test`, row-count verification, and matching SHA-256 checksums of ordered query results.
