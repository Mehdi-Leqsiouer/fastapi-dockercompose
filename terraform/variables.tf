variable "country" {
  type        = string
  description = "country id"
}

variable application_id {
  type        = string
  description = "application_id"
}

variable "project_id" {
  type        = string
  description = "The id of the GCP project."
}

variable "region" {
  type        = string
  description = "The region of the GCP project."
}

variable "environment" {
  type        = string
  default     = "dev"
  description = "Environment"
}

variable "workload" {
  type        = string
  description = "The workload for which the ressources is created"
}

variable "python_artifact_registry_purpose" {
  type        = string
  default     = ""
  description = "the purpose which will be used to build the artifact registry name"
}
variable "docker_artifact_registry_purpose" {
  type        = string
  default     = ""
  description = "the purpose which will be used to build the artifact registry name"
}

variable "repositories" {
  type        = set(map(string))
  default = []
  description = "The list of artifact repositories to create on project"
}

##############################
##         GCP APIs         ##
##############################
variable "project_services" {
  type = list(string)
  default = [
    "cloudresourcemanager.googleapis.com",
    "storage-api.googleapis.com",
    "iam.googleapis.com",
    "sql-component.googleapis.com",
    "sqladmin.googleapis.com",
    "servicenetworking.googleapis.com",
  ]
  description = "Set of services to enable on the project"
}

variable "db_name" {
  type        = string
  description = "name of the postgressql"
}

variable "db_machine_type" {
  type        = string
  description = "machine type for db instance"
}

variable "database_version" {
  type        = string
  description = "database version"
}
