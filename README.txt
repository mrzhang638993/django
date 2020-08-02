pip --default-timeout=1000 --no-cache-dir install Django==3.0.8
# 创建项目
django-admin startproject HelloWorld
# 执行如下的操作启动django 的服务器，默认的访问路径是8000端口的
python manage.py runserver
# 下面是使用python的虚拟环境搭建django服务器进行操作管理。在虚拟环境下面可以避免环境的差异性，推荐使用虚拟环境
https://www.cnblogs.com/sui776265233/p/10174646.html