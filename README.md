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
2. django 프로젝트 만들기
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
