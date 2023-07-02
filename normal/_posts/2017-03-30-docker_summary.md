---
layout: post
title: 도커 요약
---


## docker basic ##

docker search

docker pull

docker run

https://asciinema.org/a/8541tbmjqi69fe6ssw8oqpr67



## machine / compose / swarm ##

https://blog.codeship.com/docker-machine-compose-and-swarm-how-they-work-together/


* docker machine

https://docs.docker.com/machine/overview/#/whats-the-difference-between-docker-engine-and-docker-machine

https://docs.docker.com/machine/drivers/

https://docs.docker.com/machine/concepts/

* docker compose


* swarm

Finally, let’s look at the most interesting tool in the current Docker Toolbox, Docker Swarm. What you’ve done so far is work with one container host and run a container or two, which is great for testing or local development. With Docker Swarm we’re now going to turn that small test environment into a larger setup of clustered container hosts that can be used to scale your operations into something even more useful. 

https://platform9.com/blog/compare-kubernetes-vs-docker-swarm/


http://www.slideshare.net/GuillermoLucero/docker-machine-docker-swarm




https://blog.abevoelker.com/why-i-dont-use-docker-much-anymore/


## volume

ref 1 : http://container-solutions.com/understanding-volumes-docker/

ref 2 : http://pepa.holla.cz/wp-content/uploads/2016/10/Docker-in-Action.pdf

### * union file system ###
![image_layers-1-300x295.png](/img/2017_03_30/docker1.png)

**Docker images are stored as series of read-only layers. When we start a container, Docker takes the read-only image and adds a read-write layer on top. If the running container modifies an existing file, the file is copied out of the underlying read-only layer and into the top-most read-write layer where the changes are applied.** The version in the read-write layer hides the underlying file, but does not destroy it — it still exists in the underlying layer. When a Docker container is deleted, relaunching the image will start a fresh container without any of the changes made in the previously running container — those changes are lost. **Docker calls this combination of read-only layers with a read-write layer on top a Union File System.**

![04fig01_alt.jpg](/img/2017_03_30/docker2.jpg)

In order to be able to save (persist) data and also to share data between containers, **Docker came up with the concept of volumes. Quite simply, volumes are directories (or files) that are outside of the default Union File System** and exist as normal directories and files on the host filesystem.

### * volume type ###

![04fig03_alt.jpg](/img/2017_03_30/docker3.jpg)

 * Docker-managed volume

```bash
docker run -it --name vol-test -v /data centos /bin/bash

docker inspect -f "{{json .Mounts}}" vol-test | jq .
```

* Bind mount volume

```bash
docker run -it --name vol-test -v /src/sample:/data centos /bin/bash
```


Mounting a host directory can be useful for testing. For example, you can mount source code inside a container. Then, change the source code and see its effect on the application in real time.

### * Sharing Volume ###

https://docs.docker.com/compose/wordpress/

https://docs.docker.com/compose/compose-file/#volume-configuration-reference


## Docker registry

- docker image 저장 서버 : 서버에 저장하거나 s3에 저장

- docker registry도 하나의 docker image이고 docker hub에 공개되어 있음.

- `docker tag` 명령으로 태그 먼저 생성 후, `docker push`로 registry 서버에 업로드.
```bash
docker tag hello:0.1 localhost:5000/hello:0.1
docker push localhost:5000/hello:0.1
```

![docker-stages.png](/img/2017_03_30/docker4.png)


## Docker usecase

- image included source = docker managed volume


```
#!Dockerfile

# Base this docker container off the official golang docker image.
# Docker containers inherit everything from their base.
FROM golang:1.6.2

# Create a directory inside the container to store all our application and then make it the working directory.
RUN mkdir -p /src/
RUN cd /go/src/ && git clone https://github.com/surinkim/gosample.git
WORKDIR /go/src/gosample

# Copy the example-app directory (where the Dockerfile lives) into the container.
#COPY . /go/src/example-app

# Download and install any required third party dependencies into the container.
RUN go get github.com/codegangsta/gin
RUN go-wrapper download
RUN go-wrapper install


# Set the PORT environment variable inside the container
ENV PORT 8080

# Expose port 8080 to the host so we can access our application
EXPOSE 3000

# Now tell Docker what command to run when the container starts
CMD gin run
#CMD /bin/bash

```

- image excluded source = host bind volume