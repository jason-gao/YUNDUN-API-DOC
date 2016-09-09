###YUNDUN API 文档

### 关于

这是 YUNDUN API 的官方文档，我们开放了所有功能接口，包括帐户、域名、记录、监控等，你可以根据自己的需要进行程序开发。


### 在线文档

YUNDUN 官方地址：http://www.yundun.com

Github Pages: https://github.com/jason-gao/YUNDUN-API-DOC

### make
1. make clean
2. make help
3. make singlehtml
    
    
###目录结构及说明

```
YUNDUN—API-DOC
    --build
        --doctrees
        --html
    --source
        --static
        --index.rst
        --xx.rst
    --themes
        --sphinx_rtd_theme
            --static
            --__init__.py
            --theme.conf
            --xxx.html
        --YUNDUN
    --Makefile
    --README.md 
```   
+   source为源文件目录，source下conf.py为配置文件，static为静态文件目录，名字可在conf.py里配置
+   themes为主题目录，可以根据自己需求制作主题，主题目录里static为静态文件目录，其余html为对应模板文件，theme.conf为主题配置文件
+   build为编译源文件后生成的目录，可以通过make clean清空

### source/conf.py详解
1. version = '1.0'  The short X.Y version.
2. release = '1.0.1' The full version, including alpha/beta/rc tags.
3. html_theme = 'xx' 主题名，对应themes/xx
4. html_theme_options = {} 主题配置，需要主题支持
5. html_theme_path = ["../themes/"] 主题目录，相对于conf.py目录
6. html_logo = "static/logo.png" logo
7. html_static_path = ['static'] 源文件对应目录下静态文件目录,source/static
8. html_show_sphinx = False #If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
9. html_show_copyright = False #If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.


###注意
1. 当make singlehtml时，搜索好像没用，所有修改serachbox模板，当使用此命令编译时不显示搜索框




### 编译环境安装

+  Python 2.6.6
1. wget https://bootstrap.pypa.io/get-pip.py
2. python get-pip.py 安装pip
3. pip install -U Sphinx 安装Sphinx

### 安装插件

#### .md->.rst

+   https://pypi.python.org/pypi/pypandoc
+   https://github.com/listatree/convert_md_2_rst

1. pip install pypandoc
2. conf.py 取消注释sys.path.insert(0, os.path.abspath('.'))
3. extensions = ['convert_md_2_rst']添加自定义扩展配置


