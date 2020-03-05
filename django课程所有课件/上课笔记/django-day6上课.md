# Django-day6

## GenericAPIView

- 列表视图与详情视图通用：

  - **queryset** 列表视图的查询集

  - **serializer_class** 视图使用的序列化器

- 详情页视图使用：

  - **lookup_field** 

  - **lookup_url_kwarg** 



- - **get_queryset(self)**    获取结果集       self.queryset
  - **get_serializer()**    获取序列化器对象    self.get_serializer_class()  ——> return self.serializer_class


  - **get_serializer_class(self)**  获取序列化器类

  - **get_object(self)**     获取单个对象的方法    # self. get_queryset().get(pk=pk)


## 接口文档

1. 请求方式
2. 请求接口地址
3. 请求参数说明
4. 返回数据说明



## 作业

#### **用4种方式实现以下7个接口**

**7个接口**

1. 获取图书列表数据的接口

2. 获取一本图书的接口

3. 修改一本图书的接口

4. 添加一本图书

5. 删除一本图书

6. 获取最新添加的一本图书

7. 修改一本图书标题的接口


**4种方式**

1. GenericAPIView
2. GenericAPIView， 相关扩展类(ListModelMixin)
3. 子类视图（ListAPIView）
4. 视图集



## 复习

1. vue.js
2. axios
3. redis 五种数据类型


