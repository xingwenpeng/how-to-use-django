# 修改settings.py，使用mysql数据库，增加login app， 设置时区为上海

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'login',
    )

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'step02_db',
            'USER': 'root',
            'PASSWORD': 'itcast',
            'HOST': '',
            'PORT': '',
            'OPTIONS': {
                'autocommit':True,
            },
        }
    }

    TIME_ZONE = 'Asia/Shanghai'

# 在当前系统下进入mysql数据库，创建step02_db
    mysql -uusername -ppassword
    create database step02_db;

# 由于我使用的是python3.4，MySql的模块是pymysql, 需要安装pymysql


        1>. github上安装pymysql,或者用我提供给你的原码包

            git clone https://github.com/PyMySQL/PyMySQL.git

        2>. 安装需要有root权限

            cd PyMySQL
            sudo python3 setup.py install

        3>. 在python文件中直接导入
            
            import pymysql

        4>. 为了能兼容之前的代码，python2.7前的mysql组件为mysqldb

            import pysql as mysqldb

        5>. 运行一个python操作mysql的例子,测试pymysql模块


对于mysql来说，如果使用支持事务的存储引擎，那么每次操作后，commit是必须的，否则不会真正写入数据库，对应rollback可以进行相应的回滚，但是commit后是无法再rollback的。commit() 可以在执行很多sql指令后再一次调用，这样可以适当提升性能。


# 在step02项目里添加对pymysql的支持，在"step02/__init__.py"添加下面语句

    import pymysql
    pymysql.install_as_MySQLdb()

# 使用Django提供的语法检测
    python3 manage.py check



# 编写模式文件，login/models.py

# 编写模版文件，login/templates/login.html

# 编写视图文件，login/views.py


# 设置step02/urls.py

# 生成数据库
    python3 manage.py migrate

# 运行web服务器

# 打开浏览器测试
