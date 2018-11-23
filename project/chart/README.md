# 下载shape file
https://blog.csdn.net/ouening/article/details/55227364
https://github.com/ouening/python-code/blob/master/resources/CHN_adm_shp.zip
https://gadm.org/download_country_v3.html

# 安装basemap
资料：https://www.jianshu.com/p/a7020325e671
```
brew install proj
brew install geos
cd ~/Downloads/basemap-1.0.7
python3 setup.py install
```
## 安装conda
* Conda 是一个开源的软件包管理系统和环境管理系统，用于安装多个版本的软件包及其依赖关系，并在它们之间轻松切换。
### https://conda.io/miniconda.html
    通过conda安装basemap
    ```
    conda install basemap
    ```

    * 配置环境变量
    export PROJ_LIB=/Users/xujianhui/miniconda3/share/proj

## 安装 mpl-finance
    见 《 Python安装finance.txt 》 附件


