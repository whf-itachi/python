# Django-day6(重点)

## 基本视图类

### 1）APIView

#### 特点

1. 需要自定义get、post、put等请求方法，并且自己实现方法内部的所有逻辑。

2. 必须用实例化类的方式来调用序列化器，比如

   ```
   serializer = BookInfoSerializer(books, many=True)
   ```

#### 使用场景

1. 视图中实现的功能比较简单
2. 对序列化器依赖不强，只需要序列化数据，不要其他的验证，保存修改等操作
3. 不操作数据库

### 2）GenericAPIView

#### 特点

1. 同样需要自定义get、post等方法，但是可以配合扩展类，简化方法内部的逻辑

2. 为列表视图和详情视图提供了通用支持方法，比如

   ```python
   get_queryset(self)
   get_serializer(self, args, *kwargs)  可以在其他扩展类中使用
   分页过滤
   ```

3. 配合扩展，简化视图编写

#### 使用场景

1. 列表需要分页，过滤
2. 需要简化视图方法，配合扩展类

## 视图扩展类

> 扩展类必须配合GenericAPIView使用
>
> 扩展类内部的方法，在调用序列化器时，都是使用get_serializer
>
> 需要自定义get、post等请求方法，内部实现调用扩展类对应方法即可,比如：

```python
class BookListView(ListModelMixin, GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def get(self, request):
        return self.list(request)
```



### 1）ListModelMixin

1. 提供list方法，快速实现列表视图
2. 调用GenericAPIView设置好的结果集
3. 调用GenericAPIView设置好的序列化器

### 2）CreateModelMixin

1. 提供`create(request, *args, **kwargs)`方法快速实现创建资源的视图
2. 实际创建功能由序列化的save方法完成
3. save方法会去调用序列化器的create方法

### 3）RetrieveModelMixin

1. 提供`retrieve(request, *args, **kwargs)`方法，可以快速实现返回一个存在的数据对象。

### 4）UpdateModelMixin

1. 提供`update(request, *args, **kwargs)`方法，可以快速实现更新一个存在的数据对象。
2. 内部更新功能调用序列化器的save方法
3. save方法会调用序列化器的update方法

### 5）DestroyModelMixin

1. 提供`destroy(request, *args, **kwargs)`方法，可以快速实现删除一个存在的数据对象。
2. 内部模型对象的delete方法

## 子视图类

### 特点

1. 类视图中不需要自定义具体的get、post等请求方法

2. 对GenericAPIView和视图扩展类的进一步封装


### 使用场景

1. 对应不同请求，继承相应的子类视图
2. 操作模型类的情况比较多

### 1） CreateAPIView

提供 post 方法

继承自： GenericAPIView、CreateModelMixin

### 2）ListAPIView

提供 get 方法

继承自：GenericAPIView、ListModelMixin

### 3）RetireveAPIView

提供 get 方法

继承自: GenericAPIView、RetrieveModelMixin

### 4）DestoryAPIView

提供 delete 方法

继承自：GenericAPIView、DestoryModelMixin

### 5）UpdateAPIView

提供 put 和 patch 方法

继承自：GenericAPIView、UpdateModelMixin

### 6）RetrieveUpdateAPIView

提供 get、put、patch方法

继承自： GenericAPIView、RetrieveModelMixin、UpdateModelMixin

### 7）RetrieveUpdateDestoryAPIView

提供 get、put、patch、delete方法

继承自：GenericAPIView、RetrieveModelMixin、UpdateModelMixin、DestoryModelMixin



### 视图集

#### 特点

使用视图集ViewSet，可以将一系列逻辑相关的动作放到一个类中：

1. list() 提供一组数据
2. retrieve() 提供单个数据
3. create() 创建数据
4. update() 保存数据
5. destory() 删除数据
6. 自定义视图方法
7. 视图定义简单
8. 路由简单

#### 应用

1. 针对一个资源，需要使用的操作比较多
2. 操作数据库比较多
3. 使用序列化器频繁

#### 1） ViewSet

继承自`APIView`，作用也与APIView基本类似，提供了身份认证、权限校验、流量管理等。

在ViewSet中，没有提供任何动作action方法，需要我们自己实现action方法。

#### 2）GenericViewSet

继承自`GenericAPIView`，作用也与GenericAPIVIew类似，提供了get_object、get_queryset等方法便于列表视图与详情信息视图的开发。

#### 3）ModelViewSet

继承自`GenericAPIVIew`，同时包括了ListModelMixin、RetrieveModelMixin、CreateModelMixin、UpdateModelMixin、DestoryModelMixin。

#### 4）ReadOnlyModelViewSet

继承自`GenericAPIVIew`，同时包括了ListModelMixin、RetrieveModelMixin。



## 序列化器

### 序列化器类型：

#### Serializer

1. 需要自定义序列化反序列化字典
2. 需要自己实现create和update方法

#### ModelSerializer

1. 基于模型类自动生成一系列字段
2. 基于模型类自动为Serializer生成validators
3. 包含默认的create()和update()的实现

### 1）序列化

将模型对象序列化为字典

```python
serializer = BookInfoSerializer(book,many=True)
serializer.data		#获取序列化数据
# {'id': 2, 'btitle': '天龙八部', 'bpub_date': '1986-07-24', 'bread': 36, 'bcomment': 40, 'image': None}
```



### 2）反序列化

将字典反序列化为模型类对象/验证后的字典

```python
data = {'bpub_date': 123}   # 要反序列化的数据
serializer = BookInfoSerializer(data=data)   # 序列化器对象
serializer.is_valid() 		#验证
serializer.errors           #验证错误原因
serializer.validated_data   #通过验证反序列化候的数据
```



### 3）反序列化数据验证

1. 基本验证
2. 自定义验证
   1. validate_<field_name>
   2. validate
   3. validators


### 4）保存数据create，修改数据update

序列化器.save()

1. ModelSerializer自己实现
2. Serializer需要自定义 



## 补充内容

### nginx

#### 1、安装nginx软件

（1）创建一个用户组，

**#** **创建www组与www**用户

```shell
groupadd  www 

useradd  -g www -s /usr/sbin/nologin www
```

（2）解压nginx 软件，

进入到 nginx软件所在的目录，

```shell
cd nginx-1.8.1
```



（4）执行配置

```shell
./configure --user=www --group=www --prefix=/usr/local/nginx --with-http_stub_status_module --with-http_ssl_module
```

（5）执行编译安装

```
make && make install 
```

注意：安装完成后，会有4个目录

```
conf目录：配置文件所在的目录，

html目录：网站的根目录，就类似于apache里面的htdocs目录。

logs目录：是记录日志信息的目录，

sbin目录：是命令目录，
```



#### 2、nginx的启动管理

（1）启动，执行/usr/local/nginx/sbin/nginx文件，完成启动。

```
/usr/local/nginx/sbin/nginx
```

（2）测试是否启动成功

也可以使用ps aux | grep nginx  指令查询nginx的进程。

```
ps aux | grep nginx
```

```
nginx  –s stop  停止nginx的服务

nginx  –s reload 不停止nginx的服务，重新加载配置文件。
```

配置文件所在的位置：/usr/local/nginx/conf/nginx.conf



