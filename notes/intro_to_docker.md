## Intro to Docker

Sign up to DockerHub: https://hub.docker.com/

Resources: http://pyrasis.com/docker.html

| Virutal Environment      | Container (Docker)                                           |
| ------------------------ | ------------------------------------------------------------ |
| (-) File size is too big | (+) Takes out the OS component of the virtual env<br />it uses the host PC's environment and only includes necessary components<br />(+) Easy to distribute<br />(+) Easy to install OS |



#### **Install & Run Images Docker**

1. Log in as a root user: `sudo su`
2. Install docker: `cd` --> `yum install docker`
3. Log in to docker hub: `docker login`
4. Search images: `docker search centos` --> shows all images that are related to centos
5. Download images from DockerHub: `docker pull <name>`
   - With tags: `docker pull <name>:<tag>`
6. Check the list of downloaded images: `docker image ls`
   1. `ls -a` option shows all containers including the ones that are not running
7. Run the downloaded images  `docker run -t -d --name <name> <image>:<tag>`
   1. ex.  `docker run -it -d --name centos7 docker.io/centos:centos7`
   2. if centos 7 doesn't exist, it automatically downloads centos7
   3. To link ports when running docker: `docker container run -d -p <port_num> --name <name> <image>`
      - Ex. `docker container run -d -p 8000:80 --name nginx-latest nginx`
8. Check currently running container: `docker container ls` = `docker container ps`



#### Basic Commans in Docker

To pass off commands to the container: `docker exec <command>` --> execute the command inside docker exec

- Checking the version CentOS within the container: `docker exec cat /etc/redhat-release`
- Going inside the bash of the container: `docker exec -it centos7 /bin/bash`
  - result: `[root@6b083456854d /]# pwd`: 6b083456854d is the user id
- Remove container `docker container -rm -f <container_ID or name>`
- Stop container: `docker container stop <id>`
- Mapping to nginx port: `curl https://localhost:<port_num>`
  - After this step, you should be able to see the page when going into the IP: in this case, `192.168.33.10:8000` --> 8000 redirects to docker container pertaining to nginx
- Check log: `docker container logs -f <name>`



#### Creating Images Using Docker

1. Create a file to be passed off to the image: `echo "Hello, Docker." > hello-docker.txt`

2. Create Dockerfile - to be used in creating images:

   ```shell
   FROM docker.io/centos:latest
   ADD hello-docker.txt /tmp
   RUN yum install -y epel-releaese
   CMD [ "/bin/bash" ]
   ```

   

