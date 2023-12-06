# STOMP, Sock.js를 활용한 Socket 통신 구현

### STOMP란?

- Websocket 위에서 동작하며, 메시지의 유형, 형식, 내용등을 정의해 Socket 통신을 쉽게 하기 위한 양방향 통신 프로토콜
- Pub / Sub 구조로 동작
- Spring에서 기본적으로 지원하기때문에 도입 및 사용이 편리하다

### STOMP 용어 정리 (Pub, Sub, Topic, Message, Broker)

Pub(발행자)와 Sub(구독자)는 Broker를 통해 구독한 Topic에 대한 Message를 주고 받을 수 있다.

> 이해를 돕기 위한 비유 설명
>
> Pub - 발신자
>
> Sub - 수신자
>
> Broker - 우체부
>
> Topic - 우체통
>
> Message - 편지

### 구현

#### 1. Gradle dependency 추가

`build.gradle` 파일에 dependency 추가

```
1dependencies { 2	... 3	// websocket 관련 의존성 패키지 4	implementation 'org.springframework.boot:spring-boot-starter-websocket' 5	implementation 'org.webjars:webjars-locator-core' 6	implementation 'org.webjars:sockjs-client:1.0.2' 7	implementation 'org.webjars:stomp-websocket:2.3.3' 8	// frontend 코드 작성을 위한 패키지 9	implementation 'org.springframework.boot:spring-boot-starter-thymeleaf' 10	implementation 'org.webjars:bootstrap:3.3.7' 11	implementation 'org.webjars:jquery:3.1.1-1' 12	... 13	 14} 
```

 

#### 2. Controller Class 파일 작성

컴퓨터 2대에서 같은 문서를 동시 편집하고 있을때, 컴퓨터 A에서 작성된 수정사항을 컴퓨터 B로 전달할 수 있도록 매핑해주는 Controller Class 작성

1. 문서 편집이 일어나면 컴퓨터 A에서 `/topic/send` 경로로 변경사항 전달
2. `/topic/receive` 을 구독하고 있는 모든 컴퓨터들 (같은 문서를 틀고 있는 컴퓨터들)에게 업데이트된 content를 담고 있는 Document 객체 전달

```
1// 경로: /src/main/java/com/jjambbong/note/controller/WebSocketController.java 2 3@Controller 4public class WebSocketController { 5 6    @MessageMapping("/topic/send") 7    @SendTo("/topic/receive") 8    public Document test(String content) throws Exception { 9        return new Document(content); 10    } 11}
```

 

 

출처: [![img](https://zamezzz.tistory.com/favicon.ico)STOMP에 대한 이해](https://zamezzz.tistory.com/319) 

[![img](https://tistory2.daumcdn.net/tistory/4369632/d52fd1fb12274d319fddb5b05ed6f8c2)[Spring Boot\] WebSocket과 채팅 (3) - STOMP](https://dev-gorany.tistory.com/235) 