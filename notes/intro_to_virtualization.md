## Intro to Linux / Virtualization: Linux 설치하기

- 가상화(Virtualization): 기존의 하드웨어 기능들을 소프트웨어적으로 구현해 주는것
  - 대표적으로 VMware가 있음 / 수업에서는 Virtualbox 사용

- Host / guest
  - Host: 내 본체 컴퓨터
  - Guest: 소프트웨어 안에서 동작하는 os를 guest os 라고 부른다
- 가상화 환경의 사용 예
  - 개발을 할때 package 받는 등 개발환경을 복잡하게 set up 해야되는데 그 설정들을 다 가상환경에 저장해서 그 파일을 넘겨준다면 파일을 받는 사람은 별도의 set up 없이 내 프로젝트를 실행 시킬수 있음



### 가상환경 설치하기 (Setting up Virtual Environment)

1. Oracle VM Virtualbox 설치: Open-source hosted hypervisor for virtualization
   - Link to Download: https://www.virtualbox.org/wiki/Downloads
2. 필요한 파일 다운로드
   - Ubuntu Desktop (GUI): https://ubuntu.com/download/desktop
   - Ubuntu Server (CLI): https://ubuntu.com/download/server
   - Kubuntu Desktop (GUI): https://kubuntu.org/getkubuntu/

-----

#### Ubuntu 설치

1. 이름과 운영체제 설정

   1. 이름: Server
   2. 머신 폴더: C:\Linux
   3. 종류: Linux
   4. 버전: Ubuntu(64 bit)

2. RAM 메모리 설정: 2GB 정도 할당하면 충분

3. 하드 디스크 만들기: 하드디스크 종류와 어떤 방식으로 메모리를 할당할지 결정

   1. 하드 디스크 크기설정
   2. 하드 디스크 종류
      1. VDI
      2. VHD
      3. VMDK
   3. 메모리 할당 방식
      1. 동적 할당: 할당 해놓은 메모리를 언제든지 바꿀 수 있음
      2. 고정 크기: 필요한 만큼 메모리를 가상 환경에 고정 설정 해놓고 호스트 PC 에서 가상머신을 접근할 수 없게 하는 방식  - 메모리를 많이 차지하지만 더 안정적이고 빠름

4. 네트워크 설정 (VirtualBox Network 종류): 가상화 환경에서는 네트워크가 방식이나 연결되는 범위까지 설정할수 있는데 네트워크의 종류를 잘 아는 것이 중요

   1. **NAT(Network Address Translation)**: 내가 가진 네트워크를 이용해 가상 네트워크를 구축하는 방식

      <img src="https://www.nakivo.com/blog/wp-content/uploads/2019/07/VirtualBox-network-modes-%E2%80%93-how-the-NAT-mode-works.png" alt="VirtualBox network modes – how the NAT mode works" style="zoom:50%;" />

      1. 호스트 머신을 통해 외부 네트워크로 나갈 수 있음

      2. 네트워크 카드 종류가 (NAT 네트워크 대역이) 다름: IP 주소가 다름

      3. 외부에서 들어갈때는 port fowarding 방식을 이용해야 함: host machine이 gateway 역할을 함, 그러므로 외부 머신에서는 host machine만 보임

      4. 게스트와 호스트 사이의 통신만 가능
         
         

   2. **NAT Network**: NAT와 동일하나 게스트 사이의 통신도 가능

      <img src="https://www.nakivo.com/blog/wp-content/uploads/2019/07/VirtualBox-network-settings-%E2%80%93-the-NAT-Network-mode.png" alt="VirtualBox network settings – the NAT Network mode" style="zoom:50%;" />

      

      

   3. **Internal Network**: 게스트 사이의 통신은 가능하지만 외부와의 통신은 불가능(호스트 포함)

      <img src="https://www.nakivo.com/blog/wp-content/uploads/2019/07/VirtualBox-network-settings-%E2%80%93-using-the-Internal-network-mode-in-a-combination-with-the-NAT-mode.png" alt="VirtualBox network settings – using the Internal network mode in a combination with the NAT mode" style="zoom:50%;" />

      

   4. **Host-Only Adapter**: 게스트와 호스트 사이 통신, 그리고 호스트와 연결되있는 게스트간의 통신이 가능, 외부와의 통신은 불가능

      <img src="https://www.nakivo.com/blog/wp-content/uploads/2019/07/VirtualBox-network-settings-%E2%80%93-VMs-use-the-host-only-network.png" alt="VirtualBox network settings – VMs use the host-only network" style="zoom:50%;" />

   5. **Bridge Adapter**

      <img src="https://www.nakivo.com/blog/wp-content/uploads/2019/07/VirtualBox-network-settings-%E2%80%93-bridged-networking.png" alt="VirtualBox network settings – bridged networking" style="zoom:50%;" />

      1. Host의 네트워크와 Guest의 네트워크가 동일 (IP 가 같음)
      2. Guest와 외부 네트워크의 직접적인 통신이 가능
         

5. 시동 디스크 선택: 다운받아 놓은 ubuntu desktop iso 파일 선택

6. Ubuntu 운영채제 설치: 파티션 만들기 --> 포맷팅 하기

   1. 디스크 지우고 Ubuntu 설치 옵션 선택
   
   2. 그 외 국가, 언어등등 설정 완료하기
   
      

### 가상환경 설치하기 (Setting up Virtual Environment)

1. 소프트 자동 업데이트 기능 끄기
2. **root 사용자 설정**
   1. `sudo su` --> password: `ubuntu`
   2. Root id: root, root pwd: root
3. ubuntu repository 수정
4. 방화벽 재기동 및 vim, net-tools 설치
5. 자세한 정보는 이 블로그에서:
   - Ubuntu Desktop 설치:https://myanjini.tistory.com/entry/Ubuntu-Desktop-%EC%84%A4%EC%B9%98
   - Ubuntu Desktop 초기설정: https://myanjini.tistory.com/entry/Ubuntu-Desktop-%EC%B4%88%EA%B8%B0-%EC%84%A4%EC%A0%95
   - Ubuntu Server 설치: [https://myanjini.tistory.com/entry/Ubuntu-Server-%EC%84%A4%EC%B9%98](https://myanjini.tistory.com/entry/Ubuntu-Server-설치)
   - Ubuntu Server 초기설정: [https://myanjini.tistory.com/entry/Ubuntu-Server-%EC%B4%88%EA%B8%B0-%EC%84%A4%EC%A0%95](https://myanjini.tistory.com/entry/Ubuntu-Server-초기-설정)



#### Port Forwarding



![Screen Shot 2020-09-12 at 3.30.55 PM](/Users/minji/Library/Application Support/typora-user-images/Screen Shot 2020-09-12 at 3.30.55 PM.png)



Host IP: IP of the host machine (can check in mac terminal using `ifconfig`)
Host Port: assign a port that's not a duplicate

Guest IP: IP of the guest machine

Guest IP: for ssh, assign 22 for guest port

#### 그 외 설정

1. **디스플레이 설정** (자동 화면 크기 조정): 장치 --> 게스트 확장 CD 이미지 삽입
2. 클립보드 공유: 장치 --> 양방향

#### 공유 폴더 설정

Host Computer와 Guest Computer간의 공유 설정