terraform {
  required_version = ">= 1.5.0"
}

locals {
  project_name = "Multi-Cloud-Lab"
  mission      = "Mission-01"
  environment  = "local"
}

output "lab_information" {
  value = {
    project     = local.project_name
    mission     = local.mission
    environment = local.environment
    status      = "Terraform operational"
  }
}
