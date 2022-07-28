#### Authenticate GCP

`gcloud auth application-default login`

#### Initialize Terraform

`terraform init`

#### Format config

`terraform fmt`

#### Validate config files

`terraform validate`

#### Check and compare changes

`terraform plan -var="project=<gcp-project-id>"`

#### Create infrastructure

`terraform apply -var="project=<your-gcp-project-id>"`

#### Destroy the infrastructure

`terraform destroy`
