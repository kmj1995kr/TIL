# Handling Different Types of Files

###  정적 파일 (Static Files)

- image, css, js 파일과 같이 해당 내용이 고정되어 응답을 할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
- 기본 경로: `<app_name>/static/`

**기본 사용 방법**

```django
{% load static %}
static 'articles/sample.png'
```


`STATIC_ROOT`

- Django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아넣는 경로 (실제 파일이 들어있는 경로)
- collectstatic이 배포를 위해 정적 파일을 수집하는 절대 경로
- 프로젝트 배포시 사용

`STATIC_URL`

- 정적 파일을 참조 할 때 사용할 URL (실제 디렉토리가 아니고 URL로만 존재)

`STATICFILES_DIR`

- app내의 static 디렉토리 경로를 사용하는 것 외에 추가적인 정적 파일 경로 정의



### 미디어 파일 (Media Files)

- 사용자가 웹에서 업로드 하는 정적 파일
- 언제, 어느 시점에, 어떤 타입의 파일이 업로드 될지 알 수 없기 때문에 명시해주는 작업이 필요함

**기본 사용 방법**

1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정

```python
# MEDIA_ROOT는 STATIC_ROOT와 경로가 동일하면 안됨!
MEDIA_ROOT = BASE_DIR / 'media'

# 업로드 된 파일의 주소를 만들어 주는 역할 
# MEDIA_URL도 STATIC_URL과 경로가 달라야 함
MEDIA_URL = '/media/justin/'
```



1. upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로 지정
2. 업로드 된 파일의 상대 경로를 django가 제공하는 url 태그를 활용해 지정 가능

```python
# models.py
class Article(models.Model):
  ...
  image = models.ImageField(blank=True)
```

```python
# views.py
@require_http_methods(['GET', 'POST'])
def create(request):
		...
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
		...
```

