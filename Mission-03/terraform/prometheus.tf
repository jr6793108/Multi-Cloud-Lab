resource "docker_image" "prometheus" {
  name         = "prom/prometheus:v3.5.0"
  keep_locally = true
}

resource "docker_volume" "prometheus_data" {
  name = "mission03-prometheus-data"
}

resource "docker_container" "prometheus" {
  name  = "mission03-prometheus"
  image = docker_image.prometheus.image_id

  restart = "unless-stopped"

  networks_advanced {
    name = docker_network.mission03.name
  }

  ports {
    internal = 9090
    external = 9090
    ip       = "127.0.0.1"
  }

  mounts {
    target    = "/etc/prometheus/prometheus.yml"
    source    = abspath("../prometheus/prometheus.yml")
    type      = "bind"
    read_only = true
  }

  mounts {
    target = "/prometheus"
    source = docker_volume.prometheus_data.name
    type   = "volume"
  }

  command = [
    "--config.file=/etc/prometheus/prometheus.yml",
    "--storage.tsdb.path=/prometheus",
    "--web.enable-lifecycle"
  ]
}
