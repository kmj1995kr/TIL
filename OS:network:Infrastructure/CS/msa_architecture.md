# MSA 아키텍쳐 (MSA Architecture)

### 아키텍쳐 개요

MSA는 크게 Inner Architecture와 Outer Architecture로 구분지어 설명할 수 있다

**Inner Architecture**: 내부 서비스를 어떤 단위로 쪼개어서 작성할것인지를 정의한 아키텍쳐

**Outer Architecture**: 외부적으로 MSA화 되어있는 서비스를 운영하기 위해 필요한 비기능적 / 운영 관점의 아키텍쳐

<img src="https://i0.wp.com/42place.innovationacademy.kr/wp-content/uploads/2020/08/image-83.png?resize=616%2C543&ssl=1">

### Inner Architecture

Inner Architecture는 실제 서비스에 필요한 기능들을 어떻게 더 작은 단위의 서비스로 나누고, 설계하는지를 정의해 놓는 아키텍쳐를 말한다.



### Outer Architecture

Outer Architecture는 위에서도 언급했던 것처럼 Inner Architecture에서 정의된 서비스들이 정상적으로 동작할 수 있도록 지원해주는 Architecture이다. 위 그림과 같이 Gartner에서는 Outer Architecture를 6가지 구성요소로 나누어 설명한다

1. External Gateway (API Gateway)
2. Service Mesh
3. Container Management (Runtime Platform)
4. Backing Services
5. CI/CD Automation
6. Telemetry