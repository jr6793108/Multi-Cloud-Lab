resource "docker_image" "node_exporter" {
  name         = "prom/node-exporter:v1.9.1"
  keep_locally = true
}

resource "docker_container" "node_exporter" {
  name  = "mission03-node-exporter"
  image = docker_image.node_exporter.image_id

  restart = "unless-stopped"

  networks_advanced {
    name = docker_network.mission03.name
  }

  command = [
    "--path.rootfs=/host",
    "--collector.filesystem.mount-points-exclude=^/(dev|proc|sys|run/credentials|var/lib/docker/.+)($|/)"
  ]

  mounts {
    target    = "/host"
    source    = "/"
    type      = "bind"
    read_only = true
  }

  ports {
    internal = 9100
    external = 9100
    ip       = "127.0.0.1"
  }
}
