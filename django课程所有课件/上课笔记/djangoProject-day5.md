# djangoProject-day5



## 会话控制

### session

保存到session中，保存在后端。生成一个sessionid.返回时在cookie中携带sessionid



当下次请求时，浏览器会会自动携带cookie来进行请求

### Jwt

把用户信息生成一个jwt的字符串，在后端不保存，直接把jwt字符串返回给前端，手动保存jwt字符串

 

每次请求都需要手动在请求头部中携带jwt字符串

