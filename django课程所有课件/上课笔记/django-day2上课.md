# django-day2

## django三大重点：

1. 数据库操作，ORM操作
2. 序列化器
3. 视图类、扩展类



## 引入类视图的好处

1. 代码可读性、代码封装性
2. 代码复用性



## 响应

### 1. HttpResponse

```python
#第一种方式设置响应对象
HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)
content_type='Application/json'/'image/jpg'

#第二种方式设置响应对象
response = HttpResponse()
response.content='data'
response.status_code = 200/300/400/500
```

#### 响应头设置

```python
response = HttpResponse()
response['food1'] = 'hotdrynoodles'  # 自定义响应头food1, 值为hotdrynoodles
```

### 2. HttpResponse子类

Django提供了一系列HttpResponse的子类，可以快速设置状态码

- HttpResponseRedirect 301
- HttpResponsePermanentRedirect 302
- HttpResponseNotModified 304
- HttpResponseBadRequest 400
- HttpResponseNotFound 404
- HttpResponseForbidden 403
- HttpResponseNotAllowed 405
- HttpResponseGone 410
- HttpResponseServerError 500

### 3. JsonResponse

#### 作用

- 帮助我们将数据转换为json字符串
- 设置响应头**Content-Type**为 **application/json**

#### 使用

```python
from django.http import JsonResponse

def demo_view(request):
    return JsonResponse({'city': 'beijing', 'subject': 'python'},status=xxxx)
```

### 4. redirect重定向

```python
from django.shortcuts import redirect

def demo_view(request):
    return redirect(reverse('users:say'))
```

## Cookie

### 1. 设置cookie

> Cookie是服务器端设置，存储在浏览器中的一段纯文本信息

**语法**

```python
HttpResponse.set_cookie(cookie名, value=cookie值, max_age=cookie有效期)
```

**应用**

```python
def demo_view(request):
    response = HttpResponse('ok')
    response.set_cookie('itcast1', 'python1')  # 临时cookie
    response.set_cookie('itcast2', 'python2', max_age=3600)  # 有效期一小时
    return response
```

### 2. 读取cookie

```python
def demo_view(request):
    cookie1 = request.COOKIES.get('itcast1')
    print(cookie1)
    return HttpResponse('OK')
```

## Session

#### 查看sqllite数据库之前需要操作

```python
#进入项目
python manage.py makemigrations   # 生成迁移文件
python manage.py migrate    #执行迁移文件
```



### 1. 存储方式

#### 数据库

默认存储在SQLlite

```
SESSION_ENGINE='django.contrib.sessions.backends.db'
```

需要生成迁移文件，执行迁移文件生成数据表。系统已经有默认的迁移文件不需要生成。

```shell
python manage.py makemigrations	    #生成迁移文件
python manage.py migrate			#执行迁移文件
```

#### 本地缓存

```
SESSION_ENGINE='django.contrib.sessions.backends.cache'
```

#### 混合存储

```
SESSION_ENGINE='django.contrib.sessions.backends.cached_db'
```

#### Redis

**1) 安装扩展**

```
pip install django-redis
```

**2）配置**

```
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
```



**补充：  ** redis以守护进程方式启动   在配置文件中修改如下配置

```shell
136 daemonize yes    # 默认为no改为yes
```



## 类视图

### 定义

```python
from django.views.generic import View

class RegisterView(View):
    """类视图：处理注册"""

    def get(self, request):
        """处理GET请求，返回注册页面"""
        return render(request, 'register.html')

    def post(self, request):
        """处理POST请求，实现注册逻辑"""
        return HttpResponse('这里实现注册逻辑')
```

### 使用

```python
urlpatterns = [
    # 视图函数：注册
    # url(r'^register/$', views.register, name='register'),
    # 类视图：注册
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    # view --->.  dispatch
]
```

## 类视图装饰器

### 1. URL配置装饰器

```python
urlpatterns = [
    url(r'^demo/$', my_decorate(DemoView.as_view()))
]
```

### 2. 类视图中装饰

1. 为特定方法添加装饰器，重写dispatch方法

   ```python
   class DemoView(View):
       @method_decorator(my_decorator)	 # 为所有方法添加装饰器
       def dispatch(self, request, *args, **kwargs):
           return super().dispatch(request, *args, **kwargs)
       
       # 为特定请求方法添加装饰器
       #@method_decorator(my_decorator)  # 为get方法添加了装饰器
       def get(self, request):
           print('get方法')
           return HttpResponse('ok')
   
       #@method_decorator(my_decorator)  # 为post方法添加了装饰器
       def post(self, request):
           print('post方法')
           return HttpResponse('ok')
   
       def put(self, request):  # 没有为put方法添加装饰器
           print('put方法')
           return HttpResponse('ok')
   ```

2. 在类上面添加装饰器

   ```python
   @method_decorator(my_decorator, name='get')
   @method_decorator(my_decorator, name='dispatch')
   class DemoView(View):
   
       def get(self, request):
           return HttpResponse('get page')
   
       def post(self, request):
           return HttpResponse('post page')
   ```

3. 修改函数装饰器为方法装饰器

   ```python
   def my_decorator_for_class(view_func):
       def wrapper(self, request, *args, **kwargs):
           print('装饰器被调用')
           print(request.path)
           return view_func(self, request, *args, **kwargs)
   
       return wrapper
   
   
   class DemoView(View):
       @my_decorator_for_class
       def get(self, request):
           return HttpResponse('get page')
   
       def post(self, request):
           return HttpResponse('post page')
   ```

### 3. 扩展类

多继承---》mro原则

```python
class ListModelMixin(object):
    """
    list扩展类
    """
    def list(self, request, *args, **kwargs):
        ...

class CreateModelMixin(object):
    """
    create扩展类
    """
    def create(self, request, *args, **kwargs):
        ...

class BooksView(CreateModelMixin, ListModelMixin, View):
    """
    同时继承两个扩展类，复用list和create方法
    """
    def get(self, request):
        self.list(request)
        ...

    def post(self, request):
        self.create(request)
        ...

class SaveOrderView(CreateModelMixin, View):
    """
    继承CreateModelMixin扩展类，复用create方法
    """
    def post(self, request):
        self.create(request)
        ...
```

## 中间件

### 中间件定义

```python
def simple_middleware(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。

    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用。

        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。

        return response

    return middleware
```

### 中间件使用

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'users.middleware.simple_middleware',  # 添加中间件
]
```



### 中间件名称

1. 视图执行前，前置钩子/中间件
2. 视图执行后，后置钩子/中间件