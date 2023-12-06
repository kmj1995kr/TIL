공통 속성을 여러개 가지고 있는 DTO가 여러개 있다면 (예. Hist -> Master), 일일히 setter를 사용해서 한 DTO에서 다른 DTO로 매핑해주는것이 아니라 `ModelMapper` 를 사용하여 바로 매핑해줄 수 있다.

### 사용 방법
1. `pom.xml` 에 dependency 추가
```xml
<dependency>
    <groupId>org.modelmapper</groupId>
    <artifactId>modelmapper</artifactId>
    <version>2.3.8</version>
</dependency>```

2. `ModelMapperConfig` configuration 추가
우리 프로젝트의 경우 `src > main > java > ... > config` 폴더 하위에 설정 파일들을 넣어놔서 해당 폴더에 `ModelMapperConfig` 설정을 추가하였다

```java
@Configuration
public class ModelMapperConfig {

    @Bean
    public ModelMapper modelMapper(){
        return new ModelMapper();
    }
}
```

3. 사용하기
```java
// oldDTO -> newDTO로 변환하기
NewDTO newDTO = modelMapper.map(oldDTO, newDTO.class);
```

### Matching Strategy 
`ModelMapper` 는 컬럼명 같은 조건들로 자동적으로 오브젝트 매핑을 수행하기 때문에, 매핑이 수행되는 방식에 대한 Strategy를 별도로 설정해줄수 있다.
기본적으로 제공되는 Matching Strategy 는 아래 세가지가 있다.

1. STRICT
	가장 엄격한 일치 전략으로 모든 `source`와 `destination` 속성이 서로 정확히 1:1로 일치해야한다 (순서 무관)


2. STANDARD
	기본 매칭 전략으로 모든 `destination` 컬럼에 대해 정확히 일치하는 `source` 속성이 1개 있어야 한다 (순서 무관)
	`source` 컬럼은 일치하는 `destination` 속성이 한개 이상이 있어야 한다 

3. LOOSE
	마지막 `source` 와 `destination` 속성이 매칭되는 속성이 있어야 한다

### 세부 설정 하기

#### 컬럼명이 다른 경우 매핑해주기
`Source` 와 `Destination`의 컬럼명이 서로 다른 경우, `TypeMap` 을 사용하여 해당 컬럼들을 매핑해줄수 있다

```java
@Configuration
public class ModelMapperConfig {

    @Bean
    public ModelMapper modelMapper(){
			modelMapper.createTypeMap(User.class, UserDTO.class)
                .addMapping(User::getName, UserDTO::setUserName);
        return new ModelMapper();
    }
}
```

#### Custom 변환 규칙을 사용하여 매핑하기
우리 프로젝트 같은 경우, 연동 시스템에서 empty string ('') 으로 넘어오는 값들 중, DB 저장시에 null로 세팅 해주어야 되는 특정 필드들이 있었다. 이런 경우 converter를 별도 설정하여, A -> B DTO로 넘어갈때 해당 데이터가 변환 되어 넘어가도록 설정할 수 있다

아래 예제는 oldDTO의 col -> newDTO의 col을 mapping 할때, mapping 되는 값에 `emptyStringToNullConverter` 를 적용하겠다는 코드이다.

```java
@Configuration
public class ModelMapperConfig {

    @Bean
    public ModelMapper modelMapper(){
			modelMapper.using(emptyStringToNullConverter())
                .map(oldDTO::getCol, newDTO::setCol);
        return new ModelMapper();
    }
}
```