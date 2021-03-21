# Project Setting for Collaboration

### 프로젝트 세팅 순서

1. pjt 세팅
2. gitignore
3. venv 만들기

### Virtual Environment

파이썬 인터프리터, 라이브러리 및 스크립트가 "시스템 파이썬"에 설치된 모든 라이브러리와 격리 되어있는 파이썬 환경

대표적인 가상환경 지원 시스템

- **venv** --> 이걸 사용할것임!
- virtualenv
- conda
- pyenv



### 프로젝트에 venv 활용하기

1. 프로젝트 루트 폴더에 새로운 venv 생성

```bash
$ python -m venv venv
```

2. venv 활성화

```bash
$ venv venv/bin/activate
```

3. gitignore에 venv 관련된 코드 추가

4. pip을 사용하여 requirements.txt 작성

```bash
$ pip freeze > requirements.txt
```

5. Requirements.txt 활용해서 package 설치

```bash
$ pip install -r requirements.txt
```



### Fixture 사용하여 초기 데이터 불러오기

데이터를 파일에 저장하기

``` bash
$ python manage.py dumpdata --indent 4 movies movie
```

데이터 불러오기

1. 데이터 파일을 <app_name>/fixtures/<app_name> 폴더 안에 저장 (template과 똑같은 구조)
2. 데이터베이스에 데이터 저장

```bash
$ python manage.py loaddata movies/movies.json
```

