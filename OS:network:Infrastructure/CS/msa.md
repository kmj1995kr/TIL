# MSA (Micro-Service Architecture)

기존의 **Monolithic Architecture**는 하나의 어플리케이션 안에 모든 로직들이 작성되어 있는 구조로 이루어져있다. 모든 코드들이 한군데에 작성되있기 때문에 spaghetti식으로 코드들이 얼키고 설켜서 필요한 코드의 유지보수가 어렵다는것이 가장 큰 단점 중 하나였다.

그 외에도 Monolithic Architecture에는 다음과 같은 단점들이 있었다

- 개발/배포/유지보수가 어려움
- 배포가 느림
- 여러 개발자들과의 협업이 어려움: 한명이 수정하는 코드가 전체 애플리케이션에 영향을 미치기 때문
- 새로운 시스템에 빠른 반영이 어려움
- 사용자가 폭증함에 따라 확장하기 어려움
- 신기술을 반영하기 어려움
- 종속적인 라이브러리의 충돌
- 최적화되지 않은 리소스 활용 (스케일링 시 불필요한 리소스도 같이 복제됨 - 메모리 낭비)

Monolithic Architecture의 한계를 극복하기 위해 다양한 모듈화를 할 수 있는 방법론들 (Component Based Development, Service Oriented Architecture) 이 나왔지만, 현재로써 가장 널리 쓰이고 있는 MSA가 등장하게 된다. 



**MSA (Micro-Service Architecture)**란 하나의 큰 애플리케이션을 독립적이고 단순한 작은 컴포넌트 단위로 쪼개어 구축하는 아키텍쳐를 말한다.

> The term "Microservice Architecture" has sprung up over the last few years to describe a particular way of designing software applications as a suites of *independently deployable services*.

MSA Application에서는 주로:

- 각 애플리케이션이 각자의 DB, 각자의 로직을 담당하는 컴포넌트를 가지고 있다
- 애플리케이션들끼리 완전히 분리되어 동작할 수 있다
- 물리적으로 애플리케이션들끼리 분리되어 있다



<img src="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FvgBt5%2FbtqzCMNJlRr%2FMX0cps9msvAJaaoXKwApNK%2Fimg.jpg">



### MSA의 장단점

장점

- 분산형 개발을 통해 빠른 개발이 가능
- 다른 서비스에 영향을 주지 않으면서 일부분을 유지/보수 가능
- 쉽게 확장 / 결합 가능
- 각각의 모듈이 단순화되있기 때문에 개발자가 서비스를 파악하기 용이
- 각 서비스 별로 최적화된 언어, DB를 개별적으로 사용 가능

단점

- 서비스 간의 통신 (다른 모듈에 있는 데이터를 받아서 쓰는것이 어려움)
- 서비스간의 통신을 위한 아키텍쳐 설계가 복잡함
- 서비스 간의 분리로 인해 타 서비스에 종속되어 있는 애플리케이션들의 테스팅이 어려움
- API 기반의 여러 서비스를 하나의 트랜잭션으로 묶기 어려움
- API 통신 비용 증가
- 장애가 발생한 경로 추적이 어렵고, 전체적인 모니터링이 힘듬



### MSA를 도입할때 고려해야 할 사항

1. MSA가 과연 이 비지니스에 도움이 되는 아키텍쳐일까?
   - 단순히 기술 도입만을 위한 MSA가 아닌 MSA를 도입이 꼭 필요한지, 어떤 장단점이 있는지도 고려해야될 사항이다

2. 비지니스를 MSA화 한다면 어떤식으로 아키텍쳐를 구성해야될까?
   - 비지니스 전체가 MSA화 되어야될 필요는 없다!
   - 비지니스의 어떤 부분을 얼마나 큰 단위로 나눠서 아키텍쳐를 구성해야될지 고려해야된다

