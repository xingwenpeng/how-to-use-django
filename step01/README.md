# 1.生成数据库文件
    python3 manage.py migrate 

# 2.运行自带服务器
    python3 manage.py runserver

# 3.打开浏览器察看,看到欢迎界面
    127.0.0.1:8000

# 4.创建app
    python3 startapp blog

# 5.修改settings.py,添加'blog'应用
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        ***'blog',***
    )

# 6.创建view视图,打开 'blog/views.py'

    from django.shortcuts import render_to_response

    def register(req):
        return render_to_response("login.html")


# 7.创建关联view的模版文件,login.html

    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8" />
    <title>test login</title>
    </head>
    <body>
        <h1>hello world!</h1>
    </body>
    </html>

# 8.设置urls.py，增加路由

    urlpatterns = [
        # Examples:
        # url(r'^$', 'step01.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),

        url(r'^admin/', include(admin.site.urls)),
        ***url(r'^blog/$', 'blog.views.register'),***
    ]

# 9.启动django自带的web服务器
    python3 manage.py runserver


# 10.打开浏览器察看,看到"helloworld"界面
    127.0.0.1:8000/blog
