# djangoProject-day8

## redis

> Key : value

### 数据类型

**str**

数据结构：

Key : value 

特点：

value就是字符串

应用场景：

图片验证码，短信验证码

**list**

数据结构：

key： [item1, item2, item3....item1]

History_userid: [1,2,3,....]

特点：

有序，元素不唯一

应用场景：

用户浏览历史记录

**hash**

数据结构：

key： {filed1: value1, field2: value2,......}

特点：

无序，唯一，存储字段名对应字段值

应用场景：

购物车{skuid:num, skuid2:num2.....}, 用户信息{name:xxxx, age:xxxx}

**set**

数据结构：

key: (item1, item2....)

特点：

无序，唯一

应用：

购物车

**zset**(有序集合)

数据结构
key： (item1: sque1, item2:sque2, ....  )

特点：

有序，唯一

应用：

用户排行，文章点赞排行  article_id: num, article_id2: num1, 



《redis实战》  



















