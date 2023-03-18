출처: https://www.baeldung.com/spring-boot-yaml-vs-properties
https://www.latera.kr/reference/java/2019-09-29-spring-boot-config-externalize/

스프링 구조상으로 `src/main/resources` 폴더 밑에 위치하는 파일로, 스프링 프로젝트의 설정이나 환경 정보를 저장하는 파일이다.
주로, DB connection, 서버 정보등 프로젝트 전반에 필요한 환경 정보를 저장한다.

### application.properties vs. application.yml

##### 1. application.properties
스프링에서 기본으로 제공하는 형식으로 key-value를 아래의 형식으로 표현한다.
```properties
app.name=MyApp
app.description=This is my Spring Boot Application
```

List 형식의 데이터는 아래와 같이 표기할 수 있다
```properties
application.servers[0].ip=127.0.0.1
application.servers[0].path=/path1
application.servers[1].ip=127.0.0.2
application.servers[1].path=/path2
```

##### 2. application.yaml
Hierarchy 형식으로 표현하여, 가독성 있게 읽히는것이 특징이다
```yaml
app:
	name: MyApp
	description: ${app.name} is my Spring Boot Application
```

List 형식의 데이터는 아래와 같이 표기할 수 있다
```yaml
application:
	servers:
		- ip: '127.0.0.1'
		  path: '/path1'
		- ip: '127.0.0.2'
		  path: '/path2'
```


#### 장단점
- `.yaml` 파일은 계층 구조로 되어있어 키워드의 중복이 적고 가독성이 좋다
- `.yaml` 파일에서는 multi document 기능이 기본적으로 제공되어, spring boot 버전에 상관없이 한 파일에 multi profile 설정을 추가할 수 있다 (아래 내용에서 더 상세하게 설명 예정) 
- `@PropertySource` annotation을 사용하여 특정 class 파일에 property 설정을 주입할 수 있는데, 이 기능은 기본적으로는 `.properties` 파일만 사용 가능하다 (`.yaml` 파일을 사용하고자 하면 추가적인 설정 필요)

### Multiple profile 적용
프로젝트를 진행하다보면, 여러가지 운영 환경에 따라 다른 설정이 반영되어야 하는 경우가 종종 생긴다. (예를 들면, local/개발/운영 환경에서의 DB나 서버정보가 각각 다 다르기 때문에)

이럴 경우 Multiple profile을 통해 각각의 다른 운영환경에서 적용되어야 할 설정을 다르게 설정할 수 있다

##### 1. application.properties 로 설정하기
`application-{profile_name}.properties` 파일을 별도 생성한다
예를들어, 아래와 같이 local 과 개발환경에서의 서버 설정을 두가지로 설정하고 싶다면, 아래와 같이 두개 파일을 생성하고:

`application-local`
```properties
server.ip=127.0.0.1
server.path=/path1
```

`application-dev`
```properties
server.ip=172.18.209.12
server.path=/path2
```

`application.properties` 파일에서 현재 active한 profile을 지정해준다
```properties
spring.profiles.active=local
```

##### 2. application.yaml 로 설정하기
위와 예제와 같은 설정을 `.yaml` 파일에서는 하나의 파일로 설정할 수 있다
```yaml
spring:
	profiles:
		active: "local"
---
spring:
	profiles: local
server:
	ip: 127.0.0.1
	path: /path1
---
spring:
	profiles: dev
server:
	ip: 172.18.209.12
	path: /path2
```

### 외부 config 설정 주입
####  1. application.properties 파일
`application.xx` 파일 하나에서만 설정 관리를 하다보면, 양이 너무 방대해지고, 필요한 설정들끼리 모아놓고 관리를 하는것이 더욱 어려워 지게 된다.
이럴 경우, 특정 용도를 위한 config 설정은 따로 파일로 분리해 놓고 사용하는것도 가능하다

별도의 config 파일을 만든 이후, `application.properties` 파일에 아래와 같이 설정할 경우,
```
spring.config.location=classpath:/custom-config/,file:./custom-config/
```

Spring Application이 실행될때 아래의 우선순위로 configuration 파일을 적용하게 됩니다
1.  `file:./custom-config/`
2.  `classpath:custom-config/`
3.  `file:./config/`
4.  `file:./`
5.  `classpath:/config/`
6.  `classpath:/`

####  2. @PropertySource
특정 파일에만 특정 configuration 파일을 적용하고 싶을 경우, 별도의 config 파일을 만든 후 적용하고 싶은 클래스에 `@PropertySource` annotation을 사용하여, 설정을 적용할 수도 있습니다.
```java
@PropertySource(value = "classpath:custom-config.properties")
public class customClass {
	private String name;
	private List<String> aliases; // standard getter and setters
	}
```


