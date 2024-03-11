通过命令行终端 或 PyCharm都可以创建虚拟环境 venv
```shell
# 安装virtualenv
python3.12 -m pip install virtualenv

# 创建本地虚拟环境，.venv
justin@KLVC-WXX9:~/ws2/python/PycharmProjects/python-crash-course-projects/web_app$ virtualenv .venv

# 激活虚拟环境： 通过命令行
justin@KLVC-WXX9:~/ws2/python/PycharmProjects/python-crash-course-projects/web_app$ source .venv/bin/activate
(.venv) justin@KLVC-WXX9:~/ws2/python/PycharmProjects/python-crash-course-projects/web_app$ 

# 激活后都是对应当前虚拟环境，比如每个虚拟环境之间的安装包是隔离的，互不影响
(.venv) justin@KLVC-WXX9:~/ws2/python/PycharmProjects/python-crash-course-projects/web_app$ pip list
Package  Version
-------- -------
asgiref  3.7.2
Django   5.0.3
pip      24.0
sqlparse 0.4.4

# deactivate命令退出激活状态
(.venv) justin@KLVC-WXX9:~/ws2/python/PycharmProjects/python-crash-course-projects/web_app$ deactivate 

# 安装django：在对应的虚拟环境.venv被激活情况下
(.venv) justin@KLVC-WXX9:~/ws2/python/PycharmProjects/python-crash-course-projects/web_app$ python3.12 -m pip install django

```

在Pycharm中创建虚拟环境
```shell
# 创建/激活虚拟环境：通过在PyCharm的设置界面中选择Python Interpreter，没有则创建即可。

# 安装django：通过PyCharm，在设置界面中，选择对应的虚拟环境，点击“+”安装django
```

初始化Django项目：
```shell
# 创建项目 ll_project (注意命令行后面的 .)
(.venv) justin@KLVC-WXX9:~/ws2/python/PycharmProjects/python-crash-course-projects/web_app$ django-admin startproject ll_project .

# 准备数据库
(.venv) justin@KLVC-WXX9:~/ws2/python/PycharmProjects/python-crash-course-projects/web_app$ python3.12 manage.py migrate

# 启动
(.venv) justin@KLVC-WXX9:~/ws2/python/PycharmProjects/python-crash-course-projects/web_app$ python manage.py runserver
```

在项目中创建app：
```shell
# 在项目中创建app脚手架文件
(.venv) justin@KLVC-WXX9:~/ws2/python/PycharmProjects/python-crash-course-projects/web_app$ python manage.py startapp learning_logs
(.venv) justin@KLVC-WXX9:~/ws2/python/PycharmProjects/python-crash-course-projects/web_app$ ls learning_logs/
admin.py  apps.py  __init__.py  migrations  models.py  tests.py  views.py

# model数据修改后  需适配数据库
(.venv) justin@KLVC-WXX9:~/ws2/python/PycharmProjects/python-crash-course-projects/web_app$ python manage.py makemigrations learning_logs
(.venv) justin@KLVC-WXX9:~/ws2/python/PycharmProjects/python-crash-course-projects/web_app$ python manage.py migrate

# 创建超级用户 ll_admin
(.venv) justin@KLVC-WXX9:~/ws2/python/PycharmProjects/python-crash-course-projects/web_app$ python manage.py createsuperuser

```