## django-redis扩展问题

> 将session保存到redis时会报错

```python
DataError at /response/
Invalid input of type: 'CacheKey'. Convert to a byte, string or number first.
Request Method:	GET
Request URL:	http://127.0.0.1:8000/response/
Django Version:	1.11.11
Exception Type:	DataError
Exception Value:	
Invalid input of type: 'CacheKey'. Convert to a byte, string or number first.
Exception Location:	/Users/fine/.virtualenvs/django1.11/lib/python3.6/site-packages/redis/connection.py in encode, line 124
Python Executable:	/Users/fine/.virtualenvs/django1.11/bin/python
Python Version:	3.6.5
Python Path:	
['/teach/code/day2',
 '/teach/code/day2',
 '/Users/fine/.virtualenvs/django1.11/lib/python36.zip',
 '/Users/fine/.virtualenvs/django1.11/lib/python3.6',
 '/Users/fine/.virtualenvs/django1.11/lib/python3.6/lib-dynload',
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6',
 '/Users/fine/.virtualenvs/django1.11/lib/python3.6/site-packages',
 '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend']
Server time:	星期五, 16 十一月 2018 19:32:16 +0800
```



**产生原因：**

新的django-redis扩展里面的redis包版本和django中的session保存有兼容性问题



**如何解决：**

> 安装兼容的包

1. 安装好django-redis后

2. 用pip卸载关联扩展redis

   ```shell
   pip uninstall redis
   ```

3. 重新安装redis

   ```shell
   pip install redis==2.10.6
   ```
