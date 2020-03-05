# django-day1

## MVC模式

M   Model 模型，进行数据库交互							M

V    VIew  视图，封装了html，css，js，展示数据				T

C    Controll 控制器，接受请求，处理业务，响应结果			V



## 术语

项目同名目录  ===  项目管理目录

应用   === 模块（业务）

项目 === 工程



## 工程搭建

1. 创建工程

   ```python
   django-admin startproject 工程名称
   ```

2. 创建应用

   ```python
   python manage.py startapp 应用名称
   ```

3. 定义视图

   > 在应用中的views.py文件中定义

   ```python
   from django.http import HttpResponse
   
   #HttpRequest
   def index(request):
       """
       index视图
       :param request: 包含了请求信息的请求对象
       :return: 响应对象
       """
       return HttpResponse("hello the world!")
   ```

4. 路由说明

   **配置位置**：

   1. 工程同名目录下的urls.py文件，配置项目主路由

      ```python
      from django.conf.urls import url, include
      from django.contrib import admin
      # /users/say
      urlpatterns = [
          url(r'^admin/', admin.site.urls),  # django默认包含的
      
          # 添加
          url(r'^users', include('users.urls')), 
          url(r'^hotdrynoodles/', include('goods.urls')), 
      ]
      ```

   2. 应用下面，创建urls.py文件，配置属于当前应用的路由

      ```python
      #应用中配置路由
      urlpatterns = [
          url(r'^say', views.say),
          url(r'^sayhello', views.sayhello),
      ]
      ```

5. 路由命名和路由反解析

   **路由命名：**

   用来反解析对应的路由地址

   **反解析方法：**

   reverse('routename') /reverse('namespace:routename')


## 配置文件

1. BASE_DIR

   ```python
   BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
   ```

2. DEBUG

   ```python
   DEBUG=True/False
   ```

3. 项目中本地语言和时区

   ```python
   LANGUAGE_CODE = 'zh-hans'
   TIME_ZONE = 'Asia/Shanghai'
   ```



## 静态文件

```python
STATIC_URL = '/static/'			#访问路径
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_files'),   #保存静态文件目录
]
```



## 路由执行流程

由上至下, 从主路由到子路由。

## Request

### http协议向客户端传参四种形式

1. **URL地址传参.**    

   1. 视图函数（方法），传参形式获取参数

      url(r'users/index/(\d+)/(/w*)', views.index)

      1. 未命名按参数定义顺序传递
      2. 命名参数按参数名称传递

      ```python
      def fn(request, param1, param2):
          pass
      ```

2. **查询字符串.**      

   1. reques.GET

3. **请求体传参.**  

   1. request.POST.   (post请求的表单)
   2. request.body    （其他都用body来获取）

4. header头.          

   1. request.META

### QueryDict

1. HttpRequest对象的属性GET、POST都是QueryDict类型的对象

2. 特点：

   1. 一个键可以同时拥有多个值

   	​	