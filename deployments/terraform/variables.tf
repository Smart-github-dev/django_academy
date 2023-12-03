variable "application_config" {
  type    = map(any)
  default = {}
}

variable "deployment_environment" {
  default = "dev"
}


variable "deployment_endpoint" {
  type = map(any)

  default = {
    test  = "test-academy"
    dev   = "dev-academy"
    qa    = "qa-academy"
    prod  = "academy"
    stage = "stage-academy"
  }
}

variable "google_domain_name" {
  default = "fuchicorp.com"
}


## organization github token
variable "github_token" {
  default = "Please-change-this-value-to-correct-data"
}


variable "application_secret" {
  default = "application_secret"
}

variable "deployment_image" {
  default = "docker.fuchicorp.com/academy-dev:0.3"
}

variable "lets_encrypt_email" {
  default = "fuchicorpsolutions@gmail.com"
}

variable "academy_secret" {
  default = "WELCOME2019"
}

variable "vimeo_client_id" {
}

variable "vimeo_access_token" {
}

variable "vimeo_client_secret" {
}

variable "google_project_id" {
}

variable "google_bucket_name" {
}

variable "deployment_name" {
}

variable "extra_values" {
  default = ""
}
