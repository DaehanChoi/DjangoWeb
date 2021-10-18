# DjangoWeb
## 가상환경 설정
1. pyenv, pyenv-virtualenv 설치
```
brew install pyenv pyenv-virtualenv
```
2. pyenv에 가상환경 설치 / 확인
```
pyenv install 3.x.x 
pyenv versions
```
3. 가상환경 생성 및 확인
```
pyenv virtualenv 3.x.x 가상환경이름
```
4. 가상환경 실행
global 가상환경
>시스템 전역에 적용되며 따로 지정하지 않아도 기본적으로 global로 적용
local 가상환경
>특정 디렉토리 내부에서만적용됨, global시에도 무관하게 적용
```
#global
pyenv global 3.x.x
#local
~directory_name $ pyenv local django-envs 
```

## 가상환경에 Django 설치
1. django 설치
```python
python -m pip install django == 'version'
```
3. django 프로젝트 만들기
```
~directory $ django-admin startproject 프로젝트명
# 자동으로 defalut파일 생성됨
```
3. django server 실행
```
python3 manage.py startserver
python3 manage.py runserver
```
##프로젝트 구조에 대하여
>django프로젝트는 동일한 이름의 디렉토리와 그 하위 디렉토리로 나뉨
>상위 디렉토리는 project root, 하위 디렉토리는 project app으로 project app이 핵심부분을 담당함
>상위 디렉토리는 수정이 자유로움
>manage.py 프로젝트 관리의 역할 앱생성, 개발서버실행, 데이터베이스
>db.sqlite3 데이터베이스 파일
>__init__.py 하나의 python패키지로 인식시키는 역할(3.3이상에서는 괜찮지만, 하위호환을 위해 필요)
>settings.py 시간, db, 경로 설정
>urls.py url을 통해 연결해주는 역할 
>wsgi.py 연결 프로토콜

4. django app 생성, setting에 알리기
앱생성
```
python3 manage.py startapp 앱이름
```
setting.py 에 앱 알리기
![image](https://user-images.githubusercontent.com/37652653/136658204-9a97f54a-506d-4710-ba24-d5a9d649b6cd.png)


## Http 요청 만들기

1. project app 의 urls-> 앱경로 추가
```
path('appname/', include('appname.urls')) # 다음과 같은 path가 요청되었을 시 , appname패키지 urls 참고할 것 
```
2. 생성된 app에 urls 생성 후 http 요청시 response 생성가능
```
# appname/urls.py 
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index)
]
# appname/views.py
from django.http.response import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("<h2>Hello, Django</h2>")
```

## template

1. static files 관리
> 앱폴더에 static/appname 디렉토리를 생성한후 css, fonts, images 디렉토리로 나누어 각각 관리한다.
> ![image](https://user-images.githubusercontent.com/37652653/136682506-acfd5853-a5dd-4946-95ab-5bb496f2e46d.png)
```
#  html template에 static files의 사용 알리기
{% load static %}
<!DOCTYPE html>
<head>
<link rel="stylesheet" href={% static 'foods/css/syles.css' %} # 경로 설정하기
</head>
.
.
.
<div class="food"> #이미지 경로 설정도 마찬가지
      <img src={% static 'foods/images/chichen.jpg'%} width="300px" height="200px"/>
      <div class="info">
        <h3>코딩에 빠진 닭</h3>
        <P>주머니가 가벼운 당신의 마음까지 생각한 가격!</p>
        <a href="#">메뉴 보기</a>
      </div>
    </div>
```
2. template language
> 템플릿 변수
> > 지정한 데이터로 변환
```
{{변수명}} ,  {{변수명.속성}}
```
> 템플릿 태그
> > 템플릿 로직
```
{% 태그 %} {% end태그 %}
ex) for, if, with
```
> 탬플릿 필터
> > 템플릿 변수를 변환
```
{{변수명|필터}}
ex) capfirst , random, upper, lower ...
```
> 탬플릿 주석
> > 주석 처리 담당
```
{# 주석 #}
```
3. template 상속
>{% block %} 이용    
>![image](https://user-images.githubusercontent.com/37652653/136685426-78798b47-ca36-46dd-b562-6f0f55c3bbdc.png)    
>골조는 놔두고, block으로 된 부분만 상속받은 템플릿이 작성하면 됨
***

## Model/migration
>모델을 통해서 테이블을 정의하고, 장고는 DB와 연결해주는 역할을 함 -> 직접적으로 SQL query를 입력하지 않아도 됨 // ORM(Object-Relational Mapper)
>/models.py.  
>![image](https://user-images.githubusercontent.com/37652653/136698888-d7ba0dd2-e636-4dd4-a187-cc634adf99ad.png).  
1.migration
model의 변경사항이 하나의 migration
```
# migration을 생성
python3 manage.py makemigrations

# 적용
python3 manage.py migrate

# migration 사항 보기
python3 manage.py showmigrations

# 어떻게 sql로 바뀌었는지 조회가능
python3 manage.py sqlmigrate {앱이름} {마이그레이션 번호}
``` 
[Field 에 대한 공식문서](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.Field.default)

2. DB table에 맞춰 입력하기
* Shell 실행
```
python3 manage.py shell
``` 
* 모델 읽어오기
from 패키지 경로 import Menu // 쉘환경에서 python을 실행한다고 생각하면됨
* 데이터 입력 하기
```
실제 모델 필드에 맞게 내용 입력
Menu.objects.create(field_1 = "내용", field_2 = "내용"...)
```
* 조회 하기
```
Menu.objects.all() // 튜플명만 보여주기
Menu.objects.all().values() // 튜플 전체를 보여주기
Menu.objects.order_by('정렬필드')// sql order by 생각해보기
Menu.objects.filter(필드_contains='문자열')
```

* 수정 하기
```
data = Menu.objects.get(id=1)
data.필드 = '변경값'
data.save() //변경 반영
data.delete() // 데이터 삭제
```
