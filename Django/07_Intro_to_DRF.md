# Django REST Framework (DRF)

### API / REST API란?

**API (Application Programming Interface)**란 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 말한다. 즉, 코드를 통해 다른 시스템에서 제공하는 기능이나 서비스를 쉽게 사용할 수 있도록 도와주는 시스템과 시스템간의 인터페이스이다.

예를들어, 카카오 지도 같은 Open API를 생각해보면, 우리가 직접 지도의 기능을 개발하지 않아도, 카카오에서 제공하는 기본적인 지도의 기능들을 내가 작성하는 웹사이트에서 활용할 수 있다.

**REST(Representational State Transfer) API**란 웹 설계의 장점을 활용할 수 있는 아키텍쳐 방법론중에 하나로 URI와 HTTP Method를 활용해 자원을 표현한다.

- **URI:** 지정된 자원들을 가져올 수 있는 주소
- **HTTP Method:** 특정 자원에 대한 행위 (조회, 수정, 삭제...)
  - **GET**: 데이터를 받기 위한 메서드
  - **POST**: 서버로 데이터를 전송하여 변경하는 메서드
  - **PUT**: 요청한 주소의 자원을 수정하기 위한 메서드
  - **DELETE**: 자원을 삭제하기 위한 메서드
- 최종적으로 JSON 형태로 필요한 API를 client에게 제공해 준다

**Django REST Framework**란 Python 기반의 Django로 REST API를 생성할 수 있도록 도와주는 프레임워크이다.

- **Serializer**: DRF에서는 Serializer를 사용하여 내부적으로 사용하는 Queryset을 JSON으로 쉽게 변환 가능한 Python의 데이터 타입으로 바꿔주는 역할을 한다
  - ModelSerializer 클래스를 제공하여 Django의 Model을 기반으로 데이터를 serializer 해준다

<img src="https://www.seobility.net/en/wiki/images/f/f1/Rest-API.png" style="width: 50%;"></img>



### REST API 설계하기

**RESTful한 API 설계시 주의할 점**

1. 하이픈(-) 사용하기
2. 소문자 사용하기
3. 파일 확장자는 포함하지 않기
4. Method를 통해 정의되어있는 행위에 대한 표현을 URI에 중복적으로 표현하지 않기



### DRF로 REST API 구축하기

1. DRF를 설치한다

   ```bash
   $ pip install djangorestframework
   ```

2. settings.py 파일에 DRF를 추가한다

   ```python
   # settings.py
   INSTALLED_APPS = [
     ...
    	'rest_framework',
   ]
   ```

3. `urls.py` 에 API 경로를 추가한다

   ```python
   # urls.py
   urlpatterns = [
     	...
       path('json/', views.article_json),
   ]
   ```

4. Serializer 기능을 사용하기 위해 추가적으로 model이 있는 app 폴더 안에 `serializers.py` 파일을 만들어 준다

5. `serializers.py`에 serializer를 추가한다

   ```python
   # serializers.py
   from rest_framework import serializers
   from .models import Article
   
   class ArticleSerializer(serializers.ModelSerializer):
     class Meta:
       model = Article
       fields = '__all__'
   ```

6. `views.py` 에서 serializer를 활용해 API를 제공한다

   ```python
   from rest_framework.response import Response
   from rest_framework.decorators import api_view
   
   from .models import Article
   from .serializers import ArticleSerializer
   
   # http method 정의
   @api_view(['GET'])
   def article_json(request):
     articles = Article.objects.all() # 모델 데이터
     serializer = ArticleSerializer(articles, many=True) # serializer
     return response(serializer.data)
   ```

   









