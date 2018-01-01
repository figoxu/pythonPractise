```
virtualenv superset --python=python2.7
source superset/bin/activate
sudo pip install superset
```
创建账号
```
fabmanager create-admin --app superset
```

sudo superset db upgrade
sudo superset load_examples
sudo superset init
superset runserver