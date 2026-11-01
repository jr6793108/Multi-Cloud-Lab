resource "docker_image" "grafana" {
  name         = "grafana/grafana:12.1.1"
  keep_locally = true
}

resource "docker_volume" "grafana_data" {
  name = "mission03-grafana-data"
}

resource "docker_container" "grafana" {
  name  = "mission03-grafana"
  image = docker_image.grafana.image_id

  restart = "unless-stopped"

  networks_advanced {
    name = docker_network.mission03.name
  }

  ports {
    internal = 3000
    external = 3000
    ip       = "127.0.0.1"
  }

  mounts {
    target = "/var/lib/grafana"
    source = docker_volume.grafana_data.name
    type   = "volume"
  }

  mounts {
    target    = "/etc/grafana/provisioning/datasources/prometheus.yml"
    source    = abspath("../grafana/provisioning/datasources/prometheus.yml")
    type      = "bind"
    read_only = true
  }

  mounts {
    target    = "/etc/grafana/provisioning/dashboards/dashboards.yml"
    source    = abspath("../grafana/provisioning/dashboards/dashboards.yml")
    type      = "bind"
    read_only = true
  }

  mounts {
    target    = "/var/lib/grafana/mission03-dashboards"
    source    = abspath("../grafana/dashboards")
    type      = "bind"
    read_only = true
  }

  env = [
    "GF_USERS_ALLOW_SIGN_UP=false",
    "GF_AUTH_ANONYMOUS_ENABLED=false"
  ]
}
