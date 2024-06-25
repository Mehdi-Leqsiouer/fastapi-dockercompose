resource "google_artifact_registry_repository" "repositories" {
 for_each = {for re in var.repositories:  re.purpose => re}
    repository_id = replace("${var.country}-${var.workload}-${each.value.purpose}-${var.environment}", "_", "-")
    location = var.region
    labels = local.common_labels
    project = var.project_id
    description   = each.value.description
    format        = each.value.format
}
