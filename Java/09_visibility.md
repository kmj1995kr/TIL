# Java 기본 문법: Visibility (public, private, default, protected)

### public vs. private의 차이점

public / private과 같은 키워드들은 다른 클래스에서 해당 클래스를 접근하려고 할때 접근 권한을 통제하기 위한 키워드이다

- **public**: 다른 클래스에서 직접적으로 접근 가능

- **private**: 다른 클래스에서 직접적으로는 접근이 불가능하고, getter와 setter를 통해서만 접근 가능
- default: 같은 패키지 안에 있는 다른 클래스에서는 자유롭게 접근 가능
- protected



### 왜 private을 쓰는걸까?

어떤 데이터나 중요한 정보를 내가 원치않게 어떤 사람이 들어와서 접근하거나, 들어와서 바꿀 수 있다면 어떻게 될까?

지금과 같은 작은 토이 코드에서는 상관이 없겠지만, 큰 시스템, 웹사이트등에서는 내가 원하지 않는 경로로 정보를 조회, 수정하게 되면 보안 뿐만 아니라 유지 보수, 확장 측면에서도 많은 문제가 생길것이다.

이런 문제를 방지하기 위해 내가 **보호하고 싶은 정보는 private으로** 설정해두고, 대신 **public하게 사용할 수 있는 getter(조회), setter(수정) 메서드를 알맞게 제공**하여 정보를 보호할 수 있는 수단을 만들어 놓은것! 이런 것을 Data encapsulation, information hiding이라고 부른다.



### Getter와 Setter를 사용해서 private 변수 조회 / 수정하기

```java
public class Dog {
  
  // private으로 설정된 name, gender 변수
	private String name;
  private String gender = "F";
	
  // name은 조회/수정 둘다 가능
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
  
  // gender는 조회만 가능
  public String getGender() {
		return gender;
	}
	
}

```



```java
public class Test {

	public static void main(String[] args) {
		Dog coca = new Dog();
    
		coca.setName("coca");
		System.out.println(coca.getName());
		System.out.println(coca.getGender());

	}

}
```

