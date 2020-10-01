## Overview of Major Concepts

- **Unix**: [UNIX](http://en.wikipedia.org/wiki/Unix) is an operating system developed in the Bell Laboratories of AT&T and is an example a multi-tasking, multi-user operating system
  - **Characteristic of Unix:** Stable, doesn't crash, greater security & permission features, efficient
- **Linux**: Free & widely distributed Unix system
- **Kernel**: The kernel is a [computer program](https://en.wikipedia.org/wiki/Computer_program) at the core of a computer's [operating system](https://en.wikipedia.org/wiki/Operating_system) with complete control over everything in the system
- **Ubuntu**: Linux distribution based on Debian mostly composed of free and open-source software
- **Kubuntu**: Official flavour of the Ubuntu operating system that uses the KDE Plasma Desktop instead of the GNOME desktop environment



#### Network

[Intro to Network Structure](./intro_to_network_structure)

**An IP address** is a 32-bit number that uniquely identifies a host (computer or other device, such as a printer or router) on a TCP/IP network.

- **Subnet Mask** is used to determine whether the host is on the local subnet or on a remote network
  - It's used to determine exactly what device within a network the address is referring to
  - It's usually the second half or the last quarter portion of the ip address

- **Gateway**: The gate which the information flows in and out of the network

- **DNS Server**: translates alphabetical address into ip address



- **Service**: Groups the pods together in distribution
  - Outside machines only need to the service IP to access all the pods inside the service



![service diagram](/Users/minji/Downloads/service diagram.png)



#### DevOps

**Infrastructure as Code**: Codifying local development environment so that it can be easily shared and managed

- Easy to share
- Easy to maintain
- Easily to configure

**Vagrant**: Infrastructure as Code를 구현하는 가상 환경 구축 도구

- OS 가상머신의 생성, 구축, 설정을 Vagrantfile을 통해 기술할 수 있음