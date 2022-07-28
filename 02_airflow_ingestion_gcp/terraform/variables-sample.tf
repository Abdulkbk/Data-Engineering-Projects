locals {
  data_lake_bucket = "Your bucket name"
}

variable "credentials" {
  description = "Path to creds"
  default     = "path/bucket/keyfile.json change to you path"
}

variable "project" {
  description = "Project ID on GCP"
  default     = "some-project-id"
}

variable "region" {
  description = "Region for GCP resources"
  default     = "europe-north1"
  type        = string
}

variable "storage_class" {
  description = "Storage type for data lake bucket"
  default     = "STANDARD"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset name"
  default     = "some-dataset-name"
  type        = string
}
