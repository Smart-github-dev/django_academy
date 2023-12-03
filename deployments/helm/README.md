# The Academy application helm chart


you will need to first create secret with key values see example below
```
# secrets.yaml
apiVersion: v1
data:
  admin_password: 'base63'
  admin_user: 'base63'
  application_secret: 'base63'
  github_client_id: 'base63'
  github_client_secret: 'base63'
  github_token: 'base63'
  mysql_database: 'base63'
  mysql_host: 'base63'
  mysql_password: 'base63'
  mysql_user: 'base63'
  paypal_receiver_email: 'base63'
  recaptcha_private_key: 'base63'
  recaptcha_public_key: 'base63'
  vimeo_access_token: 'base63'
  vimeo_client_id: 'base63'
  vimeo_client_secret: 'base63'
kind: Secret
metadata:
  name: academy-credentials
  namespace: prod
type: Opaque
```


Example values structure
```
# values.yaml
academy:
  replicaCount: 2
  image:
    repository: "docker.fuchicorp.com/academy-stage:a501162"
    pullPolicy: IfNotPresent
  service:
    type: ClusterIP
    port: 80

ingress:
  enabled: true
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
    nginx.ingress.kubernetes.io/whitelist-source-range: '0.0.0.0/0'
    nginx.ingress.kubernetes.io/proxy-connect-timeout: "180"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "180"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "180"
  hosts:
  - host: "stage-academy.fuchicorp.com"
    paths:
    - /
  tls:
   - secretName: academy-chart-tls
     hosts:
       - "stage-academy.fuchicorp.com"
```


Set the credentials and install the helm chart into prod namespace
```
kubectl apply -f secrets.yaml
helm upgrade --install academy -n prod -f values.yaml ./academy
```

For testing and contribution will be helpfull
```
helm template --dry-run academy ./academy
```
