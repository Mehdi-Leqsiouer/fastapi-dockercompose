# Artifact Registry repositories
output "repositories_list" {
  value = {
        for r in google_artifact_registry_repository.repositories:
            r.name => {"type": "Artifact Registry repository","name": r.repository_id, "location": r.location, "format": r.format, "description": r.description}
        }
}
