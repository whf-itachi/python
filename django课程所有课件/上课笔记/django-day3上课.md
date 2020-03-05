# django-day3





## django框架重点

1. 数据库orm操作
2. 序列化器（DRF）
3. 视图类（DRF）



## datetime

### datetime.date 

> 年月日构成的日期对象
>
> [`year`](https://docs.python.org/3.6/library/datetime.html#datetime.date.year), [`month`](https://docs.python.org/3.6/library/datetime.html#datetime.date.month), and [`day`](https://docs.python.org/3.6/library/datetime.html#datetime.date.day).

1. 创建日期对象

   ```python
   today = datetime.date.today()
   d = datetime.date(1992,8,15)
   ```

2. strftime

   ```python
   today.strftime('%Y-%m-%d %H:%M:%S')
   ```

### datetime.time

> 时分秒构成具体时间
>
> [`hour`](https://docs.python.org/3.6/library/datetime.html#datetime.time.hour), [`minute`](https://docs.python.org/3.6/library/datetime.html#datetime.time.minute), [`second`](https://docs.python.org/3.6/library/datetime.html#datetime.time.second), [`microsecond`](https://docs.python.org/3.6/library/datetime.html#datetime.time.microsecond), and [`tzinfo`](https://docs.python.org/3.6/library/datetime.html#datetime.time.tzinfo).

1. 创建时间对象

   ```python
   t = datetime.time(9, 50, 20)
   ```

2. strftime

   ```python
   t.strftime('%Y-%m-%d %H:%M:%S')
   ```

### datetime.datetime

> 日期和时间
>
> [`year`](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.year), [`month`](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.month), [`day`](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.day), [`hour`](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.hour), [`minute`](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.minute), [`second`](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.second), [`microsecond`](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.microsecond), and [`tzinfo`](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.tzinfo).

1. 创建日期时间对象

   ```python
   dt = datetime.datetime.today()
   d2 = datetime.datetime(2018, 10, 1, 8, 12, 34, 2000)
   ```

2. strftime

   ```python
   dt.strftime('%Y-%m-%d %H:%M:%S')
   ```





## ORM.  对象关系映射

模型类   ---》 数据库表

模型类对象 ———》 数据表中的记录



### 关联查询

#### 一对多

> 一对应的模型类对象.多对应的模型类名小写_set 例：

```python
b = BookInfo.objects.get(id=1)

b.heroinfo_set.all()
```



#### 多对一

> 多对应的模型类对象.多对应的模型类中的关系类属性名 例：

```python
#获取多对一的关联对象
h = HeroInfo.objects.get(id=1)
h.hbook
```

```python
#获取多对一的关联id
h = HeroInfo.objects.get(id=1)
h.hbook_id
```



## 模板

### 1.配置

```python
在项目管理目录中的settings.py中设置TEMPLATES配置项的DIRS值：
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 此处修改
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 2.定义模板

1. 在项目根目录中创建templates目录用来保存所有模板

2. 在templates目录中为应用创建各自的模板目录，比如：

   `templates/users`			# 保存用户应用的模板

   `templates/goods`			# 保存商品应用的模板

   `templates/orders`			# 保存订单应用的模板


### 3.模板渲染

#### 1. HttpResponse方式

> 1. 获取模板对象
> 2. template.render(context)渲染模板

```python
from django.http import HttpResponse
from django.template import loader

def index(request):
    # 1.获取模板
    template=loader.get_template('index.html')

    context={'city': '北京'}
    # 2.渲染模板
    return HttpResponse(template.render(context))
```



#### 2. render简写方式

> render(request对象, 模板文件路径, 模板数据字典)

```python
from django.shortcuts import render

def index(request):
    context={'city': '北京'}
    return render(request,'index.html',context)
```



### 4.模板语法

#### 1. 模板变量

```python
{{变量}}
```

#### 2. 模板语句

1. for 循环
2. if 条件

#### 3. 过滤器

**语法**

```python
变量|过滤器:参数
```

#### 4. 注释

1）单行注释语法如下：

```python
{#...#}
```

2）多行注释使用comment标签，语法如下：

```python
{% comment %}
...
{% endcomment %}
```

#### 5. 模板继承

1. 父模板

   ```python
   {% block 名称 %}
   预留区域，可以编写默认内容，也可以没有默认内容
   {% endblock  名称 %}
   ```

2. 子模板

   > 标签extends：继承，写在子模板文件的第一行。

3. ```python
   {% block 名称 %}
   预留区域，可以编写默认内容，也可以没有默认内容
   {% endblock  名称 %}
   ```