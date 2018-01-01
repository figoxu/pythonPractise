```
virtualenv superset --python=python2.7
source superset/bin/activate
sudo pip install superset
```
创建账号
```
fabmanager create-admin --app superset
```
初始化并启动服务
```
sudo superset db upgrade
sudo superset load_examples
sudo superset init
superset runserver
```

汉化

通过 pip show superset ，找到 dist-package目录
找到以下目录：
cd /Users/xujianhui/PycharmProjects/pythonPractise/bigdata/analysis/visualReport/superset/superset/lib/python2.7/site-packages


修改conf.py


操作示例
https://www.youtube.com/watch?v=-kIZSuO4xjs

目前，国际化的语言，在界面上即可操作