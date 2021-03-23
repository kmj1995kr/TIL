# Django Authentication 구현하기

프로젝트와 앱 생성이 완료된 상태에서 시작

### 1. User Create

1. **urls.py** 에서 회원가입 페이지 경로 추가 (완성된 urls.py 참고)

2. 회원가입 로직을 담당할 **view** 함수 생성
   - **GET**: 회원가입 폼 띄워주기
   - **POST**: 회원가입 폼을 전송하고 회원생성

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
      	# POST 요청으로 들어온 데이터가 들어있는 폼을 로딩
        form = UserCreationForm(request.POST)
        if form.is_valid():
          	# 폼 저장
            user = form.save()
            # 저장된 유저 정보를 사용해서 로그인 하기
            auth_login(request, user)
            return redirect('accounts:index')
    else:
   			# GET 요청일시 띄워 줄 빈 로그인 폼
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/forms.html', context)
```

3. 폼이 띄워질 **template** 작성 (이후 모든 폼을 띄울 때 동일할 페이지를 사용할 것이기 때문에 forms.html이라는 하나의 파일로 생성)

```django
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  <form action="" method='POST'>
    {% csrf_token %}
    <!-- 여기서의 form이 무슨 form인지에 따라 다른 양식이 띄워짐 -->
    {% bootstrap_form form layout='horizontal' %}
    {% buttons submit="Submit" reset="Cancel" %} {% endbuttons %}
  </form>
{% endblock content %}
```

### 2. Login

1. **urls.py** 에서 로그인 페이지 경로 추가 (완성된 urls.py 참고)

2. 로그인 로직을 담당할 **view** 함수 생성
   - **GET**: 회원가입 폼 띄워주기
   - **POST**: 회원가입 폼을 전송하고 로그인
     - 이전에 있던 페이지가 있다면, 그페이지로 다시 리턴
     - 아니라면 메인 페이지로 리턴
   - 다만 이미 가입된 회원의 경우 폼을 띄워주면 안되니 다시 홈페이지로 redirect

```python
def login(request):
  	# 로그인 되있는지 체크하기
    if request.user.is_authenticated:
        return redirect('accounts:index')
		
    # 
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/forms.html', context)
```

3. **Templates** index 페이지에서 현재 상태에 따라 login 버튼을 숨김 / 표시 하기



### 3. Logout

1. **urls.py** 에서 로그아웃 페이지 경로 추가 (완성된 urls.py 참고)

2. 로그아웃 로직을 담당할 **view** 함수 생성
   - **POST**: 로그아웃 폼을 전송하고 로그인
     - 로그아웃 후 메인 페이지로 redirect
   - POST 요청만 받기
   - **로그인** 된 유저에 한해서만 폼을 보여주기

```python
...
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('accounts:index')
```



### 4. User Update

1. **urls.py** 에서 회원 정보 수정 페이지 경로 추가 (완성된 urls.py 참고)

2. **forms.py** 에서 form에서 띄워줄 정보를 customize

- 모든 정보가 아닌 이름, 이메일 정도의 기본적인 정보만 수정 가능하게 만들어야함

```python
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomerUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)
```

3. 회원 정보 수정 로직을 담당할 **view** 함수 생성
   - **GET**: 회원정보 수정 폼 띄워주기
   - **POST**: 수정된 정보를 저장
     - 현재 유저에 대한 정보가 필요함 (수정을 위해서)
     - 수정 후 메인 페이지로 redirect
   - 로그인 된 유저만 접속할 수 있게 해야함
   - 현재 유저에 대한 instance를 받아와야함 (새로운 유저가 아니라 현재 유저에 대한 정보를 수정하는 것이기 때문에)

```python
from django.contrib.auth.decorators import login_required

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomerUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomerUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/forms.html', context)
```



### 5. User Delete

1. **urls.py** 에서 delete 페이지 경로 추가 (완성된 urls.py 참고)

2. 회원 탈퇴 로직을 담당할 **view** 함수 생성
   - **POST**: 회원 탈퇴 폼을 전송하고 로그인
     - 탈퇴 후 메인 페이지로 redirect
   - POST 요청만 받기
   - **로그인** 된 유저에 한해서만 폼을 보여주기

```python
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        return redirect('accounts:index')
```



### 6. 완성된 urls, views, templates

```python
# urls.py

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
```

```python
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.views.decorators.http import require_POST

from .forms import CustomerUserChangeForm

def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # form.save에서 반환되는 객체는 이미 user기 때문에 .get_user 메서드를 사용할 필요가 없음
            user = form.save()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/forms.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/forms.html', context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('accounts:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomerUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomerUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/forms.html', context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        return redirect('accounts:index')
```

```django
<!-- index.html -->

{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  <h1>Welcome {{ user }}</h1>
  {% if user.is_authenticated %}
    <form action="{% url 'accounts:logout' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="로그아웃">
    </form>
    <form action="{% url 'accounts:delete' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="탈퇴">
    </form>
  {% else %}
    <a href="{% url 'accounts:signup' %}">회원가입</a>
    <a href="{% url 'accounts:login' %}">로그인</a>
  {% endif %}
  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi hic quia quam aspernatur nam obcaecati asperiores totam, unde assumenda commodi. Voluptas, recusandae! Deserunt totam itaque hic fuga laudantium rerum at.</p>
{% endblock content %}
```

```django
<!-- forms.html -->
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  {% if request.resolver_match.url_name == 'signup' %}
    <h1>회원가입</h1>
  {% elif request.resolver_match.url_name == 'login' %}
    <h1>로그인</h1>
  {% else %}
    <h1>회원 정보 수정</h1>
  {% endif %}
  <form action="" method='POST' name="">
    {% csrf_token %}
    {% bootstrap_form form layout='horizontal' %}
    <div class="mt-3">
      {% buttons submit="Submit" reset="Cancel" %}{% endbuttons %}
    </div>
  </form>
{% endblock content %}
```

