# ORM: DB API

### DB API

Database와 소통하기 위한 도구

**Manager**: Django 모델에 데이터베이스 query 작업이 제공되는 인터페이스

- 기본적으로 모든 django 모델 클래스에 objects라는 Manager를 추가

**Queryset**: 데이터베이스로부터 전달받은 객체 목록

- 조회, 필터, 정렬등을 수행할 수 있음



#### Queryset API

**기본 구조**

 ```python
<Class Name>.<Manager>.<QuerySet API>
 ```



### CRUD

대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능

- Create(생성)
- Read (조회)
- Update (수정)
- Delete (삭제)

#### 

##### 추가설정: Shell Plus 

shell_plus를 활용해 shell에서 orm objects CRUD 가능

```python
python manage.py shell_plus --prinit-sql
```



### 장고의 Queryset API를 활용한 CRUD 처리

**장고 Queryset API를 사용하기 위한 쉘 환경 실행 (shell로 실행시)**

1. django-extensions 설치

```python
>>> pip install django-extensions
```

2. settings.py에서 django-extensions 사용

```python
INSTALLED_APPS = [
  	...
    # third party app
    'django_extensions',
    ...
 ]
```

3. 터미널에서 shell_plus 실행

```python
>>> python manage.py shell_plus
```



**인스턴스 생성 / 저장 (CREATE)**

```python
# 방법 1
>>> article = Article()
>>> article.title = 'first'
>>> article.content = 'hello'
>>> article.save()

# 방법 2
>>> article = Article(title='second', content='hello')
>>> article.save()

# 방법 3 -- save가 필요없음!
>>> Article.objects.create(title='third', content='django')
```



**인스턴스 조회 (READ)**

```python
# 전체 조회
>>> Article.objects.all()

# 정렬
>>> Article.objects.order_by(pk)

# 검색 (인스턴스 1개만 검색 가능 - unique한 identifier로 검색해야된다)
>>> Article.objects.get(pk=1)

# 필터
>>> Article.objects.filter(content='django')
```



**인스턴스 삭제 (DELETE)**

```python
>>> article = Article.objects.get(pk=1)
>>> article.delete()
```



**인스턴스 수정 (UPDATE)**

```python
>>> article = Article.objects.get(pk=2)
>>> article.title = 'hello'
```



### Django의 Admin Site 활용하여 데이터 관리 하기

관리자 계정 만들기

```python
>>> python manage.py createsuperuser
```

<app_name>/admin.py에서 테이블 등록하기

```python
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

