# Object Relational Mapping: Model

### 기본적인 Database 용어

- **데이터베이스** (Database): 체계화된 데이터의 모임
- **쿼리** (Query): 데이터를 조회하기 위한 명령어, 조건에 맞는 데이터를 추출하거나 조작하는 명령어
- **스키마** (Schema): 데이터베이스의 구조, 표현방법 관계를 정의한 구조
- **테이블** (Table): 열과 행의 모델을 사용해 조작된 데이터 요소들의 집합 (엑셀 시트 한개와 같은 개념)
  - **필드** (Field): 열, 컬럼, 속성
  - **레코드** (Record): 행, 튜플
- **기본키** (PK: Primary Key): 각 행의 고유값으로 반드시 지정 해주어야 된다



### Object Relational Mapping (ORM)

객체 지향 프로그래밍 언어를 사용해 호환되지 않는 시스템간에 데이터를 변환하는 프로그래밍 기술 (Django - SQL)

| 장점                                                         | 단점                                           |
| ------------------------------------------------------------ | ---------------------------------------------- |
| - SQL를 잘 알지 못해도 DB 조작이 가능<br />- SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성 | - ORM 만으로는 구현하기 어려운 서비스들이 있음 |



### Model

웹 어플리케이션의 데이터를 구조화하고 조직화하기 위한 도구

- 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함: 저장된 데이터베이스의 구조

- Django는 모델을 활용하여 데이터베이스에 접근
- 모델 1개 = 데이터베이스 모델 하나에 매핑



### Migrations

Django가 model에 생긴 변화를 반영하는 방법

**대표적인 명령어**

- `makemigrations`: model을 변경한 것에 기반한 새로운 마이그레이션을 만들 때 사용 (실제 데이터베이스에 반영 X)
- `migrate`: 설계도를 실제 DB에 반영하는 과정
- `sqlmigrate`: migration 파일의 sql 변환 버전을 보여줌
- `showmigrations`: 현재 makemigrations를 통해 만들어진 파일 중 실제 migrate에 반영된 것들을 보여줌



### Migration 과정

1. 새로운 모델 추가

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.pk}번 글: <제목: {self.title} | 내용: {self.content}>'
```



2. ORM을 활용한 설계도 만들기 (Makemigrations 명령어 이용)

```bash
>>> python manage.py makemigrations
```



3. 실제 DB에 변경된 사항 반영 (Migrate 명령어 이용)

```bash
>>> python manage.py migrate
```

