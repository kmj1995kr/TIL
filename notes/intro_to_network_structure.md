## Intro to Network Structure

### Basic Concepts and Terminology

**TCP/IP**

- A **protocol** is a standard set of rules that allow electronic devices to communicate with each other
- **TCP/IP** is one of the most widely used protocol, 
- **An IP addres**s is a 32-bit number that uniquely identifies a host (computer or other device, such as a printer or router) on a TCP/IP network.
- **Subnet Mask** is used to determine whether the host is on the local subnet or on a remote network
  - It's used to determine exactly what device within a network the address is referring to
  - It's usually the second half or the last quarter portion of the ip address
- `ifconfig`: to check ip related information
- inet: ip address
- To check ip information for a designated network: `ifconfig enp0s3`

**Gateway**

- The gate which the information flows in and out of the network
- It's a hub that connects the the hosts within one network to the hosts in another network
- `ip route` can show gateway information

**DNS Server**: translates alphabetical address into ip address

**Host Name & Domain Name**

- **Domain** is an easily digestable version of IP
- **Host** refers to each computer that is attached to a local network (it's also called a **node**)
  - Within a domain, each host has to be unique
- **Peer** is a node that can give and receive information (ex.Torrent)
- **FQDN** (Fully Qualified Domain Name) - Naming convention that uniquely identifies the host within a domain (ex. cookbook.hanbit.co.kr)
- ISO OSI 7 layer

**Network Address / Braodcast Address / Netmask**



### Commands related to network setting

- `systemctl start/stop/restart/status networking`
- `ifconfig`
- `nslookup`: Checks whether the DNS server is up and running
- `ping <IP_address>`: checks whether the network signal can reach the domain

**데이터 암호화**

ssh 또는 tls를 사용해서 데이터를 암호화

통신 채널을 암호화



### Manipulating Networking Settings within Ubuntu

**Change IP Address**

Ubuntu Server 고정 IP 설정

Nic



ethernet	

Gateway (네트워크를 찾음)/router(그 안에 있는 호스트를 찾음)