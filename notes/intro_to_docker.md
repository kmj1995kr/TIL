## Intro to Docker

#### What is Docker?

- The most popularly distributed container project
  - Container technology is based on Linux Kernal
  - Integrate development, testing, management into one process
- Now supported by AWS, Google Cloud Platform, Microsoft Azure etc.
- Uses Docker Hub (It's like Github for Docker)
- 복잡한 리눅스 애플리케이션을 컨테이너로 묶어서 실행할 수 있음
- With the enhancement in the technology, hardware servers increasily became more capable of supporting mutiple servers on one hardware device
- Cloud Service: renting out the extra "server spa ce" that's not being used

Sign up to DockerHub: https://hub.docker.com/

Resources: 가장 빨리 만나는 Docker: http://pyrasis.com/docker.html

Link to Slides: https://www.slideshare.net/pyrasis/docker-fordummies-44424016?from_action=save9/

| Pros                                                         | Cons                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| - File size small compared to virtual env<br />- Takes out the OS component of the virtual env (don't need to install the entire guest OS to run containers)<br />- Uses the host PC's environment and only includes necessary components<br />- Easy to distribute / share<br />- Easy to install OS<br /> | - There are some losses in functionality --><br />to reduce this problem, CPU started supporting virtualization functionality<br />- Slow speed --> alternate solution Paravirtualization |

Docker vs. Virtual Machine

| Docker                                                       | Virtual Machine                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![Screen Shot 2020-09-14 at 11.19.59 AM](/Users/minji/Desktop/Screen Shot 2020-09-14 at 11.19.59 AM.png) | ![Screen Shot 2020-09-14 at 11.20.28 AM](/Users/minji/Desktop/Screen Shot 2020-09-14 at 11.20.28 AM.png) |



#### Immutable Infrastructure

- 한번 설치된 것을 업그레이드 하는 것이 아니라 필요에 따라서 바꿔치지 하는 시스템
- Advantages of imutable infrastructure
  - Easy to manage: You just have to manage the image
  - Scalability
  - Testing
  - Lightweight

동기 vs. 비동기

동기: One process has to end before the next process starts

- As long as the order is right,

비동기: Processes can run while waiting for the response

- 응답이 왔을때 어떻게 대응해야되는지를 명시해 놔야함 (Call bak function)

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



#### Basic Commands in Docker

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

   

