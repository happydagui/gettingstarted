# Python and Django

This is my notes for python and django.

[TOC]

## 通用环境和工具

### Vim

*Install pathogen and plugins*

	mkdir -p ~/.vim/autoload ~/.vim/bundle && \
	curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
	cd ~/.vim/bundle
	git clone https://github.com/scrooloose/nerdtree.git
    sudo pip install jedi
    git clone https://github.com/davidhalter/jedi-vim.git
    git clone https://github.com/terryma/vim-multiple-cursors.git

~/.vimrc

	execute pathogen#infect()
	syntax on
	filetype plugin indent on

> 自动检测文件类型并加载对应配置

    autocmd FileType python setlocal et sta sw=4 sts=4

> 自动替换tab为4个空格
> :NERDTree 可以显示目录，ctr+w+h 光标移到左侧树形目录，ctrl+w+l 光标移到右侧文件显示窗口。多次摁 ctrl+w，光标自动在左右侧窗口切换

### zealdoc - programming document allinone

    sudo add-apt-repository ppa:zeal-developers/ppa
    sudo apt-get update
    sudo apt-get remove appmenu-qt5
    sudo apt-get install zeal

## Python

### Installation and Configuration

*installation*

    wget https://bootstrap.pypa.io/get-pip.py
    sudo python get-pip.pyp
    sudo pip install virtualenv
    sudo pip install virtualenvwrapper
    vi ~/.bashrc
    source ~/.bashrc

*.bashrc*
    # at the end of .bashrc, add
    source /usr/local/bin/virtualenvwrapper.sh

*Create Environ*

Virtual env is saved in ~/virtualenvs/, you can set WORKON_HOME to change it.

    mkvirtualenv py2
    mkvirtualenv -p /usr/bin/python3 py3

*Install other packages via pip*

    # before installing other 
    sudo apt-get install python-dev python3-dev
    workon py2(3)
    (py2)pip install xxxx
>> install from github: `pip install git+https://github.com/pika/pika.git` git+后面是你的git地址，打开github页面后，有一个地方可以复制url的，就是那个。

### Samples

pip install lxml httplib2

- python 3

    workon py3
    pip install Pillow
    pip install django django-debug-toolbar django-ckeditor
    pip install mysql-connector-python --allow-external mysql-connector-python
    pip install gunicorn uwsgi
    pip install pymongo
    pip install beautifulsoup4



### 

*Mysql and drivers*

    sudo apt-get install mysql-server libmysqld-dev libmysqlclient-dev
    (py2)pip install MySQL-python
    (py3)pip install mysql-connector-python --allow-external mysql-connector-python
> Install `libmysqld-dev libmysqlclient-dev` when mysql_config not found.
> use `'ENGINE': 'django.db.backends.mysql',` for MySQL-python with django
> use `'ENGINE': 'mysql.connector.django',` for mysql-connector-python with django

*Nginx*

    sudo apt-get install nginx
    sudo /etc/init.d/nginx start
    sudo vi /etc/nginx/site-available/default

/etc/nginx/site-available/default

    location / { 
        # First attempt to serve request as file, then 
        # as directory, then fall back to displaying a 404. 
        try_files $uri $uri/ #404; 
        # Uncomment to enable naxsi on this location 
        # include /etc/nginx/naxsi.rules 
    } 
    # Example for serving static resources
    location /static { 
        alias /home/min/media/sdb1/workspaces/happycc/openexam/static/;
    } 

*RabbitMQ*

Install and Start/Stop

    sudo apt-get intall rabbitmq-server
    sudo rabbitmqctl stop
    sudo rabbitmq-server
    sudo rabbitmq-server -detached  # run in background
    sudo rabbitmqctl stop

Python Client:

- pika (python 2.x only): ```pip install pika```
- pika (for python 3.x): ``pip install git+https://github.com/pika/pika.git````
Python MQ Framework

    pip install celery
    pip install django-celery

*Memcached*

    sudo apt-get install libevent-dev
    wget http://memcached.org/latest
    tar -zxvf memcached-1.x.x.tar.gz
    cd memcached-1.x.x
    ./configure && make && make test && sudo make install
    memcached -h
    memcached -d -vv # -d -> daemon, -vv -> show message
    ps aux|grep memcached
    killall memcached

- python-memcached(python 2 only)
    wget ftp://ftp.tummy.com/pub/python-memcached/python-memcached-latest.tar.gz
    tar -zxvf python-memcached-latest.tar.gz
    python setup.py install

    import memcache
    mc = memcache.Client(['localhost:11211'])
    mc.set('foo', 'bar', 10)
    mc.get('foo')

in django

	CACHES = {
	'default': {
	'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
	'LOCATION': [
	'172.19.26.240:11211',
	'172.19.26.242:11211',
	]
	}
	}

- pylibmc (python 3 ok)
    sudo apt-get install libmemcached-dev 
    pip install pylibmc

in django

	CACHES = {
	'default': {
	'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
	'LOCATION': [
	'172.19.26.240:11211',
	'172.19.26.242:11211',
	]
	}
	}

> see <http://sendapatch.se/projects/pylibmc/>
> django 中的cache产生的key，value，直接通过pylibmc访问时，有个:1:前缀

    from django.core.cache import get_cache
    ch = get_cache('django.core.cache.backends.memcached.PyLibMCCache')
    ch.set('hello', 'hello world')
    ch.get('hello')
    # mc.get(':1:hello') # for non-django env

> 同样非django中通过pylibmc设置 ```mc.set(':1:foo', 'bar')```可以在django中通过```cc.get('foo')```访问
> 启动memcache不加-d参数，可以在控制台看到被访问的key名称

> 可以在memcache中存储各种类型的python对象，基本类型、类、函数
> 例如：```import math;mc.set('foo', math.sqrt)```，取出是可以直接
> 使用 ```mc.get('foo')(4)```
> 类实例的话，需要类的定义已经import了。


**Redis**

INSTALL

sudo apt-get install redis-server
ps aux|grep redis
netstat -nlt|grep 6379
redis-cli
sudo service redis-server start/stop
sudo /etc/init.d/redis-server start/stop

PYTHON Client

    pip install redis

> Getting Started
>    >>> import redis
>    >>> r = redis.StrictRedis(host='localhost', port=6379, db=0)
>    >>> r.set('foo', 'bar')
>    True
>    >>> r.get('foo')
>    'bar'

### Python libraries

* Whitenoise
* Phonenumbers
*  *Pdfkit*

## Django

### Django Auth

**urls.py**

    url(r'^accounts/', include('django.contrib.auth.urls')),

**settings.py**

    LOGIN_REDIRECT_URL # '/main/'
    LOGIN_URL # '/accounts/login/'

**add your template pages, `registration/login.html` for example.**

### aggregation and annotate
aggregation -> 
annotate -> one to many

> order_by is required for annotate

##django-braces

##django-ckeditor

see <https://github.com/django-ckeditor/django-ckeditor>,<http://www.nanerbang.com/article/2/>

    pip install Pillow
    pip install django-ckeditor
    python manage.py collectstatic

settings.py

    INSTALLED_APPS # (
        #...
        'ckeditor',
        #...
    )

urls.py
    #...
    url(r'^ckeditor/', include('ckeditor.urls')),
    #...

models.py

    from ckeditor.fields import RichTextField,CKEditorWidget
    class Question(models.Model):
        question_id # models.AutoField(primary_key#True)
        question_subject # models.ForeignKey(Subject)
        # question_description # models.TextField()
        question_description # RichTextField(u'题目')

alternative in forms.py

    from ckeditor.fields import RichTextField,CKEditorWidget
    class QuestionForm(forms.ModelForm):
        class Meta:
            model = Question
            exclude =  []
            widgets = {
                'question_description': CKEditorWidget(),
            }

in the template

    <form role#"form" id#"theform" method#"post">
    {% csrf_token %}
        {{ form.as_p }}
        <input type#"submit" class#"" />
    </form>
    {{ form.media }}

> {{form.nedia}} must be after the jquery.js, its output is as below:

    <script type#"text/javascript" src#"/static/ckeditor/ckeditor/ckeditor.js"></script>
    <script type#"text/javascript" src#"/static/ckeditor/ckeditor-init.js"></script>

> local variable 'visible_filename' referenced before assignment, you should set `filebrowserBrowseUrl` as the media resource url.

    CKEDITOR_UPLOAD_PATH='upload'
    CKEDITOR_CONFIGS # {
        'default': {
            'toolbar': 'Full',
            'filebrowserBrowseUrl': 'http://directory.apache.org/api/download/download-archive.html',
            'filebrowserImageBrowseUrl': 'http://localhost/static/',
        },
    }

> TODO: 后台列表页面的RichText字段会显示html内容，如何去除？

##django debug toolbar

- settings.py

    INSTALLED_APPS # (
        #...
        'django.contrib.staticfiles',
        'debug_toolbar',
        # ...
    )
    MIDDLEWARE_CLASSES # (
        'debug_
.middleware.DebugToolbarMiddleware',
        # ...
    )
    DEBUG # True

- urls.py

    if settings.DEBUG:
    import debug_toolbar
    urlpatterns +# patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)))

- run `python manage.py collectstatic` before runserver

### Django Notes
####django template and autoscape

**display html content**

    {% autoescape off %}{{ question_description }}{% endautoescape %}

**去除html内容中的html标签，比如图片、换行、分段等**

    { obj.question_description|removetags:'img p div' }}

## Deploy django

### gunicorn

    pip install gunicorn
    gunicorn openexam

### uwsgi
    pip install uwsgi
    touch uwsgi.ini & vi uwsgi
    sudo mkdir -p /var/log/uwsgi
    sudo chown min:min /var/log/uwsgi
    uwsgi --ini uwsgi.ini

    [uwsgi]
    chdir=/home/min/media/sdb1/workspace/happcc/openexam
    module=openexam.wsgi:application
    master=True
    socket=127.0.0.1:8000
    pidfile=/tmp/openexam-master.pid
    vacuum=True
    max-requests=5000
    #daemonize=/var/log/uwsgi/openexam.log

**Questions:**

> (py3dj)min@T410:~/media/sdb1/workspaces/happycc/openexam$ uwsgi --ini uwsgi.ini [uWSGI] getting INI configuration from uwsgi.ini
*** Starting uWSGI 2.0.11.1 (64bit) on [Mon Jul 27 16:22:50 2015] ***
compiled with version: 4.8.4 on 27 July 2015 16:05:16
os: Linux-3.16.0-43-generic #58~14.04.1-Ubuntu SMP Mon Jun 22 10:21:20 UTC 2015
nodename: T410
machine: x86_64
clock source: unix
detected number of CPU cores: 4
current working directory: /home/min/media/sdb1/workspaces/happycc/openexam
writing pidfile to /tmp/openexam-master.pid
detected binary path: /home/min/.virtualenvs/py3dj/bin/uwsgi
!!! no internal routing support, rebuild with pcre support !!!
chdir() to /home/min/media/sdb1/workspace/happcc/openexam
chdir(): No such file or directory [core/uwsgi.c line 2581]
VACUUM: pidfile removed.
chdir(): No such file or directory [core/uwsgi.c line 1603]

### uwsgi + nginx



### FAQ for pip

*libxml/xmlversion.h: No such file or directory*

    sudo apt-get install libxml2-dev libxslt1-dev

*EnvironmentError: mysql_config not found*
    
    sudo apt-get install libmysqlclient-dev

*numpy.distutils.system_info.NotFoundError: no lapack/blas resources found*

    sudo apt-get install liblapack-dev libblas-dev texinfo libicu-dev 

*__main__.ConfigurationError: Could not run curl-config: [Errno 2] No such file or directory*

    sudo apt-get install libcurl4-openssl-dev

*fatal error: sqlfront.h: No such file or directory*

    sudo apt-get install freetds-dev 

*library dfftpack has Fortran sources but no Fortran compiler found*

    sudo apt-get install gfortran

*fatal error: cups/cups.h: No such file or directory*

    sudo apt-get install libcups2-dev

*fatal error: openssl/aes.h: No such file or directory*

    sudo apt-get install libssl-dev

*fatal error: libsmbclient.h: No such file or directory*

    sudo apt-get install libsmbclient-dev

fatal error: ffi.h: No such file or directory

    sudo apt-get install libffi-dev

fatal error: openssl/aes.h:No such file or directory

    sudo apt-get install libssl-dev

InsecurePlatformWarning: A true SSLContext object is not available.

    sudo apt-get install libffi-dev libssl-dev
    (env)pip install pyopenssl ndg-httpsclient pyasn1