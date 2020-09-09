## Intro to DevOps

#### Waterfall vs. Agile

**Waterfall**

![Agile Vs Waterfall in Software Development - Ultimate Guide by Saigon  Technology](https://saigontechnology.com/assets/media/agile-scrum-vs-waterfall.png)



- **Infrastrcture as Code**: codifying development, operation process so that it is easily accessible



#### Set up Infrastructure as Code Using Vagrant

**Vagrant**: Vagrant is an open-source software product for building and maintaining portable virtual software development environments

*To be able to use VirtualBox 6.1, you must use Vagrant 2.2.1 or higher*

1. Power off all other virtual environments
2. Install Vagrant
3. Create a working directory `mkdir ~/HashiCorp/WorkDir`
4. Create Vagrantfile: inside WorkDir `vagrant init`
5. Edit Vagrantfile
6. Create a new virtual machine and run it