resource "kubernetes_secret" "academy_credentials" {
  metadata {
    name      = "academy-credentials"
    namespace = var.deployment_environment
  }

  data = {
    github_token       = var.github_token
    application_secret = var.application_secret

    ## Getting all values from vimeo variable
    vimeo_client_id     = var.vimeo_client_id
    vimeo_access_token  = var.vimeo_access_token
    vimeo_client_secret = var.vimeo_client_secret

    ## Getting all mysql values from mysql map
    mysql_user     = lookup(var.application_config[var.deployment_environment], "mysql_user")
    mysql_database = lookup(var.application_config[var.deployment_environment], "mysql_database")
    mysql_password = lookup(var.application_config[var.deployment_environment], "mysql_password")
    mysql_host     = lookup(var.application_config[var.deployment_environment], "mysql_host")

    ## Getting admin_user admin_password github_client_id github_client_secret from django map
    admin_user           = lookup(var.application_config[var.deployment_environment], "admin_user")
    admin_password       = lookup(var.application_config[var.deployment_environment], "admin_password")
    github_client_id     = lookup(var.application_config[var.deployment_environment], "github_client_id")
    github_client_secret = lookup(var.application_config[var.deployment_environment], "github_client_secret")

    ## Getting recaptcha configuration
    recaptcha_public_key  = lookup(var.application_config[var.deployment_environment], "recaptcha_public_key")
    recaptcha_private_key = lookup(var.application_config[var.deployment_environment], "recaptcha_private_key")

    ## Getting receiver email from paypal map
    paypal_receiver_email = lookup(var.application_config[var.deployment_environment], "paypal_receiver_email")

    ## Getting the slack webhook endpoint
    slack_webhook_endpoint = lookup(var.application_config[var.deployment_environment], "slack_webhook_endpoint")
  }
}
