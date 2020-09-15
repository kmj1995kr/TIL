## Lab Exercise Creating & Running a Web Server Image

##### Method 1: Create a container using Ubuntu image and modify the container to create the image

Start from docker

1. Create a working directory: `mkdir ~/webserver && cd ~/webserver`

2. Create hello.html file: `echo "hello docker" > hello.html

3. Using the Ubuntu image, run a container on the background: `docker container run -dit -p 8080:80 --name myweb ubuntu:14.04`

4. Go inside the container

   - `docker container exec -it myweb /bin/bash`

   - `docker container attach <container_name>`

5. Install webserver from inside the container

   1. `apt-get update`
   2. `apt-get install apache2 -y`
   3. Check whether apache2 is running: `service apache2 status`
   4. Start apache if it's not running: `service apache2 start`
   5. exit out of the container: `exit`

6. Copy hello.html to apache webserver web route: `docker container cp ./hello.html myweb:/var/www/html/`

   1. To check whether it has copied over correctly: `docker container exec myweb cat /var/www/html/hello.html`

7. Request a webservice through container: `curl http://localhost:8080/hello.html`

8. Create an image: `docker commit myweb kmj1995kr/myweb:latest`



##### Method 2: Create an image using Dockerfile

Start from docker

1. Create a dockerfile:

   ```bash
   FROM ubuntu:14.04
   
   RUN apt-get update
   
   RUN apt-get install -y apache2
   
   ADD hello.html /var/www/html/
   
   EXPOSE 80
   
   CMD apachectl -DFOREGROUND
   ```

2. Build an image using the dockerfile: `docker image build -t kmj1995kr/myweb:dockerfile`
3. Run the container using the created image: `docker container run -d -p 9090:80 --name mywebdockerfile kmj1995kr/myweb:dockerfile`
   - To randomly assign the port: `docker container run -d -P --name mywebdockerfile kmj1995kr/myweb:dockerfile`
4. Request a webservice through container: `curl http://localhost:9090/hello.html`



##### Method 3: Run the server using existing image

1. Search image from dockerhub
2. Download (pull) image: `docker pull image` (ex.) `docker pull nginx`
3. Create nginx server (and run): `docker container run --name webserver -d -p 80:80 nginx` --> `curl http://localhost`



Creating a Blog Service with using wordpress & mysql

1. Create a working directory: `mkdir ~.blog && cd ~/blog`
2. Run mysql container: `docker run -d --name <name> -e MYSQL_ROOT_PASSWORD=<password> -e MYSQL_DATABASE=<db_name> mysql:5.7`
3. Run webserver using Wordpress