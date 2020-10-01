## Intro to DevOps

#### Waterfall vs. Agile

**Waterfall**

![Agile Vs Waterfall in Software Development - Ultimate Guide by Saigon  Technology](https://saigontechnology.com/assets/media/agile-scrum-vs-waterfall.png)



- **Infrastrcture as Code**: codifying development, operation process so that it is easily accessible



**Why is this needed?**

- It's difficult to collaborate when everyone in the team has a different development environment
- By creating vagrant files (virtual environment), everyone can share the same environment when developing the service
- It's easy to install and set up
- It's easy to debug (there are less issues coming from environmental differences)



#### Set up Infrastructure as Code Using Vagrant

**Vagrant**: Vagrant is an open-source software product for building and maintaining portable virtual software development environments

Details: https://docs.google.com/document/d/1-ik6BpcuibHxiqNbilSHrovzALM8G2G2eEFFmVbPxQ4/edit#heading=h.l625pp4r7ecp

*To be able to use VirtualBox 6.1, you must use Vagrant 2.2.1 or higher*

1. Power off all other virtual environments

2. Install Vagrant

3. Create a working directory `mkdir ~/HashiCorp/WorkDir`

4. Create Vagrantfile: inside WorkDir `vagrant init`

5. Edit Vagrantfile

   ```bash
   # -*- mode: ruby -*-
   # vi: set ft=ruby :
   
   Vagrant.configure("2") do |config|
     config.vm.box = "generic/centos7"  #base image to be used
     config.vm.hostname = "minji"				 #host_name
     config.vm.network "private_network", ip: "192.168.33.10"		#ip of the VM
     config.vm.synced_folder ".", "/home/vagrant/sync", disabled: true		#sync options with the host machine
   end
   ```

   

6. Create a new virtual machine and run it: `vagrant up`

7. Run and go into the new virtual machine
   - Use VirtualBox
   - Use terminal: `vagrant ssh`
   - Use ssh client (e.g. Putty)

8. Basic Vagrant Commands

   1. Create snapshots: `vagrant snapshot --save`
   2. Turn off vagrant VM: `vagrant halt`
   3. Print username: `whoami`
   4. Print hostname: `uname -n`

9. Delete vagrant: `vagrant destroy` - same as delete all files on VirtualBox



##### Why use Vagrant instead of VM created from ISO Images? (Pros of Infrastructure as Code)

*Creation --> Setting --> Maintanence in one*

- Can easily share environments
- Can easily figure out different settings in the environments (all laid out in the vagrant code)
- Can easily maintain the environment



#### Provisioning

#### Set up Infrastructure Using Ansible

1. Check whether nginx is install or not: `systemctl status nginx`
2. Install Ansible 
   1. `sudo systemctl stop nginx.service`: stop nginx that's currently running
   2. `sudo yum install -y epel-release`
   3. `sudo yum install -y ansible`
   4. `ansible --version`: check ansible version
3. Run nginx using ansible
   1. `sudo sh -c "echo \\"localhost\\" >> etc/ansible/hosts"`
   2. `cat /etc/ansible/hosts`
   3. `ansible localhost -b -c local -m service -a "name=nginx state=started"`
      1. `localhost`: Out of the servers in the inventory file, designates which server would execute the command
      2. `-b`: user of the designated server; -b = root
      3. `-c local`: since the connecting server is within my pc, instead of using ssh, using local server
      4. `m service`: name of the module that ansible will use --> in this case `service`
      5. `"name=nginx state=started"`: other parameters
   4. Check whether `"changed": true` --> means that the status has been changed --> this indicated that the system is now running
4. Check nginx status: `systemctl status nginx.service`



#### Ansible Playbook Install

1. Install git: `sudo yum install -y git`

2. Create a ansible-playbook-sample repository clone: `git clone https://github.com/devops-book/ansible-playbook-sample.git`

3. Execute and set up playbook

   1. `cd ansible-playbook-sample/`
   2. `ansible-playbook -i deveopment site.yml`: `development` designates the location of this install (default `/etc/ansible/hosts`)
   3. `curl localhost`
   4. `ansible-playbook -i production site.yml`
   5. `curl localhost`

4. Check the host that is currently executing the server (when calling `curl`)

   1. `cat development` - under [development-webservers] in results it shows localhost
   2. =means that user localhost is executing under the development server

5. Check the definition of `curl`

   1. `ls ./roles/nginx/tasks/main.yml`
   2. `cat ./roles/nginx/tasks/main.yml`

6. Check the template:  `cat ./roles/nginx/templates/index.html.j2`

7. Check where the variables are being called from: `cat ./group_vars/development-webservers.yml`

8. Change the template: `vi ./roles/nginx/templates/index.html.j2` --> make any change

9. Execute in a dry-run mode: Doesn't actually change the file, but mock runs and shows the results

   `ansible-playbook -i development site.yml --check --diff`

   - `--check`: executes in dry-run mode
   - `--diff`: shows what has been changed



| Vagrant                                                      | Ansible                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| + Easy to use<br />- Depending on the person ways of setting up might be diff<br />- Hard to scale to multiple environment | + More structured<br />+ Easy to customize/manage by different environments<br />+선언적, 추상화, 수렴화, 역동성, 간소화, 자동화? |



#### Automation of Infrastructure Testing Using Serverspec

**Serverspec**

- A tool that helps testing (including infrastructure settings testing)
- Can format test results in a designated format
- Can export it in a printable format

**Installing Serverspec using Ansible**

1. Add Serverspec role in the Playbook file
2. Check Serverspec role: `cat ./roles/serverspec/tasks/main.yml`
3. Install serverspec using ansible-playbook: `ansible-playbook -i development`



host PC에서 ip 접속 안될 경우 방화벽 체크

`systemctl status firewalld` --> active라면

`sudo systemctl stop firewalld`

