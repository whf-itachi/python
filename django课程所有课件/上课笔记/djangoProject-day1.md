# 美多商城-day1



## 美多项目目录结构

```python
meiduo					 	#项目目录
	front_end_pc		 	#前端文件目录
    meiduo_mall			 	#django后端项目目录
    	docs				#文档目录
        logs			 	#日志目录
        meiduo_mall			#项目管理目录(django项目同名目录)
        	apps			#应用目录
            libs			#第三方库目录
            settings		#配置文件目录	 [prod.py,dev.py]
            utils			#自定义库目录
        scripts				#脚本文件目录  [shell脚本、python脚本]
        manage.py			#自动化脚本	
```



## linux操作系统生成秘钥对

```shell
ssh-keygen -t rsa  [-C "xxxxx@xxxxx.com"]

#操作完后，会生成.ssh目录
#复制id_rsa.pub里面的内容到马云  （ssh公钥的位置）
```



## 添加密钥到ssh-agent

```shell
eval "$(ssh-agent -s)"     # start the ssh-agent in the background
ssh-add ~/.ssh/id_rsa	   # add
```



## 准备工作

1. 创建新的虚拟环境

2. 安装项目需要的包

   ```python
   pip install django==1.11.11
   pip install djangorestframework
   pip install pymysql
   ```



## 项目学习重点

1.  业务流程

2.  技术点



### 业务流程举例

注册功能：

1. 接受客户端数据

2. 校验参数， 用户名是否存在

3. 数据入库

4. 保存会话状态 

5. 响应


### 技术点举例

页面静态化原理

会话认证方式： session     JWT 



## 学习项目注意

1. 不要一边看视频一边跟着敲代码，如果有需要只需要记关键点，记自己不清楚的点。流程梳理清楚，在动手写代码

2. 碰到问题bug，要自己先抽几分钟解决， 然后在寻求帮助。要有自己解决问题的意识，也要慢慢培养自己解决问题的能力




























