output "application_deployed" {
  value = "${lookup(var.deployment_endpoint, var.deployment_environment)}.${var.google_domain_name}"
}
output "whitelisted_ranges" {
  value = lookup(var.application_config[var.deployment_environment], "whitelisted_cidrs")
}
