# 练习参考文档
https://www.pythonsheets.com/notes/python-sqlalchemy.html

# 配置 pip下载的加速

mkdir ~/.pip
cat > ~/.pip/pip.conf << EOF
[global]
trusted-host=mirrors.aliyun.com
index-url=http://mirrors.aliyun.com/pypi/simple/
EOF

# 安装依赖 sqlalchemy
pip install sqlalchemy
pip install psycopg2

pip install psycopg2-binary

