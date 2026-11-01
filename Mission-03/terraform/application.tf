resource "docker_image" "mission03_app" {
  name         = "mission03-web:v1"
  keep_locally = true
}

resource "docker_container" "mission03_app" {
  name  = "mission03-web"
  image = docker_image.mission03_app.image_id

  restart = "unless-stopped"

  networks_advanced {
    name = docker_network.mission03.name
  }

  ports {
    internal = 8080
    external = 8081
    ip       = "127.0.0.1"
  }

  env = [
    "APP_VERSION=1.0"
  ]
}
