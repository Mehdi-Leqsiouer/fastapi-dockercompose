terraform {
  required_version = ">= 1.3.5"

  backend "http" {
    lock_method    = "POST"
    unlock_method  = "DELETE"
    retry_wait_min = 5
  }
}

# Enable required services on the project
resource "google_project_service" "service" {
  count   = length(var.project_services)
  project = var.project_id
  service = element(var.project_services, count.index)

  # Do not disable the service on destroy. On destroy, we are going to
  # destroy the project, but we need the APIs available to destroy the
  # underlying resources.
  disable_on_destroy = false
}


locals {
  # template labels for all resources
  common_labels = {
    "country" = var.country
    "environment" = var.environment
    "application-id" = var.application_id
  }
}
