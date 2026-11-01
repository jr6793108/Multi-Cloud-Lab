provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_network" "mission03" {
  name = "mission03-network"
}
