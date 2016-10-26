from __future__ import with_statement
from datetime import datetime
from fabric.api import local
from fabric.api import *
from fabric.colors import green
#from fabric.contrib.console import confirm

env.hosts = ['montecatiniterme.ivirgilius.com@95.110.198.140']
env.user = 'montecatiniterme.ivirgilius.com'
env.use_ssh_config = False
code_dir = 'private/django'
restart_apache_command = "touch montecatini/wsgi.py"


app_list = [
    'montecatini',
    'montecatini_ccn',
    'montecatini_events',
    'montecatini_map',
    'montecatini_metro',
    'montecatini_news',
]

languages = [
    'it',
    'en',
    'es',
    'de',
    'ru',
    'fr',
    'zh',
]

db_username = 'ivirgilius'
db_password = '8Mkjmdh6BL'
db_name = 'montecatiniterme'



def test():
    local("./manage.py test")


def commit():
    local("git add -p && git commit")


def push():
    local("git push")


def prepare_deploy():
    commit()
    push()


def makemessages():
    for app in app_list:
        with lcd(app):
            print(green(app))
            for language in languages:
                local("mkdir -p locale/%s" % language)
                local("../manage.py makemessages --symlinks --no-obsolete --locale=%s -v 0" % language)
                local("git add locale/%s/LC_MESSAGES/django.po" % language)
            local("../manage.py compilemessages")


def compilemessages():
    for app in app_list:
        with lcd(app):
            print(green(app))
            local("../manage.py compilemessages")


def deploy():
    with cd(code_dir):
        run("git stash")
        run("git pull")
        run("git submodule update --init")
        #run("cp patches/cms_toolbar.py cms/cms_toolbar.py")
        #run("cp patches/pageadmin.py cms/admin/pageadmin.py")
        run("source env/bin/activate && pip install -r requirements.txt --no-deps")
        run("source env/bin/activate && ./manage.py collectstatic --noinput --clear")
        run("source env/bin/activate && ./manage.py compilemessages")
        #for app in app_list:
        #    with cd(app):
        #        print(green(app))
        #        run("../manage.py compilemessages")
        run("source env/bin/activate && ./manage.py migrate")
        run(restart_apache_command)


def sync():
    filename = 'database_backup_{0:%Y%m%d_%H%M}.sql'.format(datetime.now())

    print(green("Exporting main database data to %s..." % filename))
    run("mysqldump --add-drop-table --user=%s --password=%s %s > private/%s" % (db_username, db_password, db_name, filename))

    print(green("Fetching main database file..."))
    run("cd private && gzip %s" % filename)
    get("private/%s.gz" % filename, "%s.gz" % filename)
    run("rm private/%s.gz" % filename)
    local("gunzip %s.gz" % filename)

    print(green("Importing main database data..."))
    local("mysql -u root -e \"CREATE DATABASE IF NOT EXISTS %s;\"" % db_name)
    local("mysqladmin -u root --force drop %s" % db_name)
    local("mysqladmin -u root create %s" % db_name)
    local("mysql -u root %s < %s" % (db_name, filename))
    local("rm %s" % filename)

    print(green("Syncronizing main media..."))
    local("rsync -chavzP --stats %s:private/django/media/ media" % env.hosts[0])

    print(green("Applying migrations..."))
    local("./manage.py migrate")

    print(green("Rebuilding locales..."))
    local("./manage.py compilemessages")

    print(green("Done."))
