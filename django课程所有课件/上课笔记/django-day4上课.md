# Django-day4

## video

## 表单使用流程

1. 自定义表单类
2. 视图中使用
   1. 实例化表单类，模板渲染时返回给客户端
   2. 验证表单数据，实例化表单类（传入参数request.POST），验证表单数据



## web开发模式

1. ### 前后端分离

   返回数据类型： json、xml

   ```python
   json：
   '[{"name":"iphone", "price"：88}, {"name":"ipad", "price":99}, ...]'
   
   xml:
   <goods>
   	<good>
       	<name>iphone</name>
           <price>88</price>
       </good>
       <good>
       	<name>ipad</name>
           <price>99</price>   	
       </good>
       ....
   </goods>
   ```


2. ### 前后端不分离

   返回渲染后的html数据

   包括html、css、js



## restFul风格

### 主要是url地址的设计

```python
GET /goods/
POST /goods/
PUT /goods/1/
DELETE /goods/1/
```



### 接口四要素

1. 接口地址
2. 接口请求方式
3. 接口参数
4. 返回的字符串格式json、xml、html
5. 接口开发文档很重要



###  restful风格接口定义要点

1. 请求方式
2. 请求的接口地址
3. 数据格式的转换



### 接口返回数据

```python
{
    "data":{}/[{},{},{}]/xxxxxs
    "msg":'成功/失败/参数不正确',
    "statuscode": 200/300/400/500
}
```

