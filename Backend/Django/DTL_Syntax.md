# DTL Syntax

#### Django에서 지켜야할 Syntax

- `/` 붙이기
- trailing comma

#### DTL Syntax란?

**DTL**: Django template에서 사용하는 built-in template system

쉽게 말하면 장고에서만 사용하는 특수한 언어라고 생각하면 됨!

- 조건, 반복, 변수 치환, 필터등의 기능을 제공
- 참고: https://docs.djangoproject.com/en/3.1/ref/templates/language/

**4가지 메인 요소**

1. Variables
2. Filters
3. Tags
4. Comments

#### Variables

**Views.py:** render의 세번째 인자로 넘겨주고 싶은 값들은 {key: value}의 딕셔너리 형태로 넘겨줌

- 가독성과 유지보수를 위해 context 변수에 원하는 값들을 한꺼번에 넘겨줄 수 있음
- context 안에 있는 key와 value의 이름은 통일성을 위해 맞춰주는것이 일반적

```python
def greetings(request):
  foods = ['apple', 'banana', 'coconut',]
  context = {
    'name': 'Minji',
    'foods': foods,
  }
  return render(request, 'greetings.html', context)
```

**Template/<html파일>:** html template 파일에서 다음과 같이 사용 가능

```html
...
<body>
  <h1>Hello, my name is {{ info.name }}!</h1>
  <p>My fav food: {{ foods.0 }}</p>
</body>
...
```



#### Filter

표시할 변수의 출력을 수정할 때 사용 가능 (template 딴에서)

예를들어, 메뉴의 길이를 출력하고 싶을때 다음과 같이 코드를 작성하면 됨

```html
<body>
  <h1>오늘 저녁은 {{ pick }}</h1>
  <p>{{ pick }}의 길이는 {{ pick|length }}</p>
</body>
```



#### Tags

- `{% function %}` 형태로 사용한다
- for, if 문 등을 템플릿에서 처리할때 사용한다



#### Comments

- **Single Line Comment**: `{# #}`
- **Multi LIne Comments**: `{% %}`



#### Template Inheritance

- `{% extends %}`: 템플릿 최상단에서 부모의 템플릿을 상속받아 확장하는 것
- `{% block %}`: 하위 템플릿에서 채워질 공간을 마련해놓는 것