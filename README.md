

# 需求分析
## 网管管理
网管是管理员，有多个，可以登录、添加会员、查看所有会员、删除会员、编辑会员信息

## 会员管理
会员是普通用户，不能登录，

# 开发
## 数据库迁移
```python
python manage.py makemigrations

python manage.py migrate
```

# 运行
```python
python manage.py runserver 0.0.0.0:9999
```