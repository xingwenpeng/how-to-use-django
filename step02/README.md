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

    from django.db import models


    class user_register(models.Model):
        user_name = models.CharField(max_length = 30, default = None)
        user_email = models.EmailField()
        user_passwd = models.CharField(max_length = 30, default = None)
        register_date = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.user_name


    class pr(models.Model):
        photo_id = models.CharField(max_length=20)
        photo_path =models.CharField(max_length=200)
        photo_size = models.IntegerField()
        photo_type = models.CharField(max_length=8)
        browse_times = models.IntegerField(default=1)
        user_name = models.CharField(max_length = 30, default =None)
        photo_date = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.photo_path , self.photo_size


# 编写模版文件，login/templates/login.html


    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8" />
    <title>我拍我世界</title></title>
    </head>
    <body>
        {% if form.error %}
        <p>error !</p>
        {% endif %}
        <form action="" method="post">
            <table>
                {{ form.as_table }}		
            </table>
            <input type="submit" value="登录"></input>
        </form>	
        
    </body>
    </html>

# 编写视图文件，login/views.py


    from django.shortcuts import render
    from django.shortcuts import render_to_response
    from django import forms
    from login.models import user_register
    from django.http import HttpResponse

    class ContactForm(forms.Form):
        user_name = forms.CharField(max_length=100, label='用户名')
        user_email = forms.EmailField(label='Email')
        user_passwd = forms.CharField(widget=forms.TextInput(attrs={'type':'password'}), label='密码')
        #user_passwd = forms.CharField()

    def register(request):
        if request.method == 'POST':
            form = ContactForm(request.POST);
            if form.is_valid():
                persion = form.cleaned_data
                name = persion['user_name']
                password = persion['user_passwd']
                email = persion['user_email']
                user = user_register(user_name=name, user_passwd=password, user_email=email);
                user.save()
                return HttpResponse('ok')
            else :
                return HttpResponse('form err')
        else :
            form = ContactForm();
        return render_to_response('login.html', {'form': form})
                


# 关闭settings.py中的csrf服务


    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        #'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    )

# 设置step02/urls.py

    urlpatterns = [
        # Examples:
        # url(r'^$', 'step02.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),

        url(r'^admin/', include(admin.site.urls)),
        url(r'^login/register$', 'login.views.register'),
    ]

# 生成数据库
    python3 manage.py makemigrations
    python3 manage.py migrate

# 运行web服务器
    python3 manage.py runserver

# 打开浏览器测试
    127.0.0.1:8000/login/register

# 看到注册用户界面，录入测试数据

# 在命令行中登录mysql，察看是否保存了刚才用户提交的数据
