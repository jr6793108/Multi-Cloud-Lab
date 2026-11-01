# Mission-03: Infrastructure Monitoring and Observability

## Business Problem

Cloud operations teams need reliable visibility into application
availability, request traffic, response latency, and infrastructure
resource utilization.

Without centralized monitoring, service degradation may go
undetected and troubleshooting becomes reactive.

## Solution

Designed and deployed a containerized monitoring environment
using Terraform, Docker, Prometheus, Node Exporter, and Grafana.

The solution provides:

- Repeatable infrastructure deployment with Terraform
- Containerized Python application exposing Prometheus metrics
- Application and infrastructure metrics collection
- Grafana dashboards provisioned from configuration files
- Persistent monitoring data storage
- Local-only management ports with SSH tunnel access
- Validation of monitoring behavior using generated HTTP traffic

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Terraform | Infrastructure as Code |
| Docker | Container runtime and networking |
| Python | Instrumented web application |
| Prometheus | Metrics collection and storage |
| Node Exporter | Infrastructure metrics |
| Grafana | Monitoring dashboards |
| Ubuntu Linux | Host operating system |

## Architecture

See [Architecture Documentation](documentation/architecture.md).

## Monitoring Dashboard

The Grafana dashboard contains six panels:

1. Application Availability
2. HTTP Requests per Second
3. HTTP Response Latency
4. CPU Utilization
5. Memory Utilization
6. Root Filesystem Utilization

Dashboard definition:

[grafana/dashboards/mission03-monitoring.json](grafana/dashboards/mission03-monitoring.json)

## Deployment

From the terraform directory:

```bash
terraform init
terraform validate
terraform plan
terraform apply
```

The application image must be built locally before deploying
Terraform resources. Refer to the application Dockerfile.

## Validation

The environment was tested using:

- Docker container status checks
- Prometheus target health queries
- Grafana health endpoint
- Application HTTP request generation
- Grafana performance dashboards
- Terraform validate and plan

Final Terraform verification:

```text
No changes. Your infrastructure matches the configuration.
```

See [Monitoring Evidence](evidence/monitoring-validation.txt).

## Security Considerations

- Monitoring web ports bind to 127.0.0.1
- Remote browser access uses SSH port forwarding
- Grafana anonymous access is disabled
- Grafana user sign-up is disabled
- Terraform state files and credentials must not be committed

## Project Outcome

Implemented and validated a repeatable monitoring environment
providing visibility into application health and infrastructure
performance through Prometheus and Grafana.

## Portfolio Focus

Cloud Engineering | Infrastructure as Code | Docker |
Monitoring | Observability | Linux Operations
