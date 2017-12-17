
#安装virtualenv

```
sudo easy_install virtualenv
sudo pip3 install -i http://mirrors.aliyuncs.com/pypi/simple virtualenv
```

#初始化virtualenv

```
virtualenv -p /usr/local/bin/python3 venv
```

#激活venv的环境
```
. venv/bin/activate
```

#在venv的环境中安装flask
```
pip3 install --upgrade --trusted-host pypi.douban.com  -i  http://pypi.douban.com/simple flask
```
PyPI国内源
* 阿里云 http://mirrors.aliyun.com/pypi/simple/
* 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
* 豆瓣(douban) http://pypi.douban.com/simple/
* 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
* 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

