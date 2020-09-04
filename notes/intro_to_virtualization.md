## Intro to Virtualization

- 가상화(Virtualization): 하드웨어 기능들을 소프트웨어적으로 구현해 주는것
  - 대표적으로 VMware가 있음

- Host / guest
  - Host: 내 본체 컴퓨터
  - Guest: 소프트웨어 안에서 동작하는 os를 guest os 라고 부른다



### 가상환경 설치하기 (Setting up Virtual Environment)

1. Oracle VM Virtualbox 설치: Open-source hosted hypervisor for virtualization
   - Link to Download: https://www.virtualbox.org/wiki/Downloads
2. 필요한 파일 다운로드
   - Ubuntu Desktop (GUI): https://ubuntu.com/download/desktop
   - Ubuntu Server (CLI): https://ubuntu.com/download/server

-----

#### Ubuntu 설치

1. 이름과 운영체제 입력

   1. 이름: Server
   2. 머신 폴더: C:\Linux
   3. 종류: Linux
   4. 버전: Ubuntu(64 bit)

2. RAM 메모리 설정: 2GB 정도 할당하면 충분

3. 하드 디스크 만들기: 하드디스크 종류와 어떤 방식으로 메모리를 할당할지 결정

   1. 하드 디스크 종류
      1. VDI
      2. VHD
      3. VMDK
   2. 메모리 할당 방식
      1. 동적 할당: 할당 해놓은 메모리를 언제든지 바꿀 수 있음
      2. 고정 크기: 필요한 만큼 메모리를 가상 환경에 고정 설정 해놓고 호스트 PC 에서 가상머신을 접근할 수 없게 하는 방식  - 메모리를 많이 차지하지만 더 안정적이고 빠름

4. 네트워크 설정 (VirtualBox Network 종류): 가상화 환경에서는 네트워크가 방식이나 연결되는 범위까지 설정할수 있는데 네트워크의 종류를 잘 아는 것이 중요

   1. **NAT(Network Address Translation)**: 내가 가진 네트워크를 이용해 가상 네트워크를 구축하는 방식

      <img src="/Users/minji/Downloads/nat.png" style="zoom:40%;" />

      1. 호스트 머신을 통해 외부 네트워크로 나갈 수 있음
      2. 네트워크 카드 종류가 (NAT 네트워크 대역이) 다름: IP 주소가 다름
      3. 외부에서 들어갈때는 port fowarding 방식을 이용해야 함: host machine이 gateway 역할을 함, 그러므로 외부 머신에서는 host machine만 보임
      4. 게스트와 호스트 사이의 통신만 가능
         

   2. **NAT Network**

      <img src="/Users/minji/Downloads/nat network.png" style="zoom: 40%;" />

      1. NAT와 동일하나 게스트 사이의 통신도 가능
         

   3. **Internal Network**

      <img src="/Users/minji/Downloads/internal.png" style="zoom:40%;" />

      1. 게스트 사이의 통신만 가능
      2. 외부와의 통신은 불가능
         

   4. **Host-Only Adapter**

      <img src="/Users/minji/Downloads/host-only.png" style="zoom:40%;" />

      1. 게스트와 호스트 사이의 통신만 가능
      2. 외부와의 통신은 불가능
         

   5. **Bridge Adapter**

      <img src="/Users/minji/Downloads/bridge.png" style="zoom:40%;" />

      1. Host의 네트워크와 Guest의 네트워크가 동일 (IP 가 같음)
      2. Guest와 외부 네트워크의 직접적인 통신이 가능
         

5. Ubuntu 운영채제 설치: 파티션 만들기 --> 포맷팅 하기