module "academy" {
  source                 = "fuchicorp/chart/helm"
  version                = "v0.2.1"
  deployment_name        = "academy"
  deployment_environment = var.deployment_environment
  deployment_path        = "../helm"
  remote_chart           = "true"
  enabled                = "true"
  remote_override_values = <<EOF
academy:
  replicaCount: "${lookup(var.application_config[var.deployment_environment], "application_replicas")}"
  image:
    repository: "${var.deployment_image}"
    pullPolicy: IfNotPresent
  service:
    type: ClusterIP
    port: 80

ingress:
  enabled: true
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
    nginx.ingress.kubernetes.io/whitelist-source-range: "${lookup(var.application_config[var.deployment_environment], "whitelisted_cidrs")}"
  hosts:
  - host: "${lookup(var.deployment_endpoint, var.deployment_environment)}.${var.google_domain_name}"
    paths:
    - /
  tls:
   - secretName: academy-chart-tls
     hosts:
       - "${lookup(var.deployment_endpoint, var.deployment_environment)}.${var.google_domain_name}"
EOF
}
