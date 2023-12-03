# How to run the academy with docker compose?
This documentation describes how to run the academy using [docker compose](https://docs.docker.com/compose/gettingstarted/).

## Before you begin
1. Make sure you have docker is installed
2. Make sure docker-compose is installed


First you will need to clone the repo
```
git clone git@github.com:fuchicorp/academy.git
```


after you cloned you will need to get into `academy/deployments/docker`
```
cd academy/deployments/docker
```


You should see docker file and docker-compose file to build and make it up and running
```
ls -la
drwxrwxr-x.  3 fsadykov fsadykov   66 Apr 11 19:16 .
drwxrwxr-x.  5 fsadykov fsadykov   89 Feb 20 17:32 ..
drwxrwxr-x. 14 fsadykov fsadykov 4096 Apr 11 19:51 academy
-rw-rw-r--.  1 fsadykov fsadykov  870 Apr 11 20:34 docker-compose.yaml
-rw-rw-r--.  1 fsadykov fsadykov  862 Apr 11 20:22 Dockerfile
```


Docker compose has environment variables configured see below all env
```
export GIT_TOKEN='<YOUR GITHUB TOKEN>'
```


After you have everything set up you can go ahead and start build and deploy
```
docker-compose build
docker-compose up
```


## List of environment variables
| Environment variable  | Required      | Description
| --------------------- |-------------- | -----------
| GIT_TOKEN             | yes           | To pull information from github
| GITHUB_CLIENT_ID      | no            | To configuration github auth
| GITHUB_CLIENT_SECRET  | no            | To configuration github auth
