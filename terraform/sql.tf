resource "google_sql_database_instance" "default" {
  name                = var.db_name
  project             = var.project_id
  region              = var.region
  database_version    = var.database_version
  deletion_protection = false

  settings {
    tier = var.db_machine_type
    ip_configuration {
      ipv4_enabled                                  = false
      private_network = google_compute_network.private_network.id
      enable_private_path_for_google_cloud_services = true
      require_ssl                                   = false
    }
  }
}
