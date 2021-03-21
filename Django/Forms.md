# Django: Forms

### Django에서 Form으로 데이터를 받고 전송하는 과정

1. Form이 만들어질 throw.html 페이지를 생성한다
2. 데이터를 전달하기 위해 form을 생성하고 input field를 작성한다
3. 

### Form 만들기

**1. Form이 만들어질 throw.html 페이지를 생성한다**

urls.py

```python
urlpatterns = [
		...
    path('throw', views.throw, name="throw"),
]
```

views.py

```python
def throw(request):
    return render(request, 'throw.html')
```

templates/throw.html

```django
{% extends 'base.html' %}
{% block content %}
  <div class="container" style="margin-top: 50px;">
  </div>
{% endblock %}
```



**2. 데이터를 전달하기 위해 form을 생성하고 input field를 작성한다**

- `action`: 다음 보내질 경로
- `for`: 어떤 input의 label인지 명시해주는 속성
- `name`: 저장될 데이터의 key값에 해당 (key를 변수처럼 활용해서 호출할 수 있게 된다)
- `value`: 저장될 데이터의 value값에 해당 (text field는 자동으로 value가 text에 입력한 값이 된다)

```django
{% extends 'base.html' %}
{% block content %}
  <div class="container" style="margin-top: 50px;">
    <form action="catch">
      <label for="my_val">아무거나 입력하세요: </label>
      <input type="text" name="my_val" id="my_val">
      <input type="submit" value="전송">
    </form>
  </div>
{% endblock %}
```



**3. 데이터를 전달받기 위한 catch.html 페이지를 생성한다**

urls.py

```python
urlpatterns = [
		...
    path('throw', views.throw, name="throw"),
  	path('catch', views.throw, name="catch"),
]
```

views.py

```python
def catch(request):
    # 이렇게 해도 나오지만 일반 파이썬 코딩과 똑같이 이렇게 딕셔너리 접근을 하면 에러처리가 안된다
    # my_val = request.GET['my_val']
    # .get 메서드는 GET 메서드랑은 상관없이 dictionary 접근할때 쓰는 파이썬 내장 .get method
    my_val = request.GET.get('my_val')
    context = {
        'my_val': my_val,
    }
    return render(request, 'catch.html', context)
```



```django
{% extends 'base.html' %}
{% block content %}
  <h1>Hello</h1>
  <p>{{ my_val }}</p>
{% endblock %}
```

