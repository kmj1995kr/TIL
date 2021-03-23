# Django CRUD 구현하기

1. 프로젝트 생성

```bash
$ django-admin startproject <project_name>
```

2. .gitignore 파일 생성

```bash
$ touch .gitignore
```

gitignore.io 에서 필요한 설정 파일 검색 후 복사 --> 붙여넣기

3. 가상환경 생성

```bash
$ python -m venv venv
```

3-1. 가상환경 activate

```bash
$ source venv/bin/activate
```

4. 패키지 설치 (optional: 이전 프로젝트를 pull 받아서 requirements 파일이 있는 경우)

```bash
$ pip install -r requirements.txt
```

5. 데이터 로딩 (optional: 협업 환경에서 만들어 진 불러올 데이터가 있는 경우)

   1. 데이터 파일을 <app_name>/fixtures/<app_name> 폴더 안에 저장 (template과 똑같은 구조)
   2. 데이터베이스에 데이터 저장

   ```bash
   $ python manage.py loaddata movies/movies.json
   ```


6. settings.py에서 기본 세팅 바꾸기

```python
TEMPLATES = [
  {
    'DIRS': [
      BASE_DIR / '<app_name>' / 'templates'
    ]
  }
]
...
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```

7. 기본 생성 테이블 migrate 하기

```bash
$ python manage.py migrate
```

8. 서버 실행 시켜 보기

```bash
$ python manage.py runserver
```

9. app 만들기

```bash
$ python manage.py startapp <app_name>
```

10. settings.py에서 앱 추가

```python
# settings.py
INSTALLED_APPS = [
  '<app_name>',
  ...
]
```

11. base template 만들기
    - 프로젝트 폴더에서 templates 폴더 만들기
    - Base.html 생성 후 원하는 템플릿 파일
    - 부트스트랩 CDN등 포함하기 (getbootstrap에서 가져온 CDN을 활용하거나, django의 django-bootstrap5 활용)

12. app의 urls include 하기

```python
# <project>/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<app_name>/', include('<app_name>.urls')),
]
```

13. app에서 urls.py 파일과 templates/<app_name> folder 생성

14. app의 urls.py 에서 페이지 url 생성

