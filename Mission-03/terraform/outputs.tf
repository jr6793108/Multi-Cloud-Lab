output "mission03_network_name" {
  description = "Docker network created by Terraform"
  value       = docker_network.mission03.name
}

output "mission03_network_id" {
  description = "Docker network ID"
  value       = docker_network.mission03.id
}

output "mission03_application_name" {
  description = "Mission-03 application container name"
  value       = docker_container.mission03_app.name
}

output "mission03_application_url" {
  description = "Local application URL"
  value       = "http://127.0.0.1:8081"
}

output "prometheus_url" {
  description = "Prometheus local web interface"
  value       = "http://127.0.0.1:9090"
}

output "prometheus_container" {
  description = "Prometheus container name"
  value       = docker_container.prometheus.name
}

output "grafana_url" {
  description = "Grafana local web interface"
  value       = "http://127.0.0.1:3000"
}

output "grafana_container" {
  description = "Grafana container name"
  value       = docker_container.grafana.name
}
