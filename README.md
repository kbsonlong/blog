# 1.1、下载源码

git clone https://github.com/kbsonlong/SaltRuler.git

# 1.2、安装依赖

pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com

# 1.3、同步数据库

python manage.py makemigrations

python manage.py migrate

