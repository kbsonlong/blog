# 1.1、下载源码

git clone https://github.com/kbsonlong/blog.git

# 1.2、安装依赖

pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com

# 1.3、同步数据库

python manage.py makemigrations

python manage.py migrate

# 1.4、创建后台管理员

    # python manage.py createsuperuser
    Username (leave blank to use 'root'): admin
    Email address: kbsonlong@gmail.com
    Password:
    Password (again):
    Superuser created successfully.

# 1.5、安装并[配置uwsgi](/config/uwsgi.ini)

pip install uwsgi

# 1.6、 [配置nginx](/config/nginx.conf)


# 1.7、启动uwsgi和nginx

uwsgi --ini config/uwsgi.ini

/etc/init.d/nginx start

