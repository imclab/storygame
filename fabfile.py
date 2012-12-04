from fabric.api import local
import os

FAB_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.basename(os.path.dirname(__file__))
PROJECT_TEMPLATE = "https://github.com/nowherefarm/django-project-template/archive/master.zip"

def startproject():
    local("django-admin.py startproject --template=%s %s ." % (
        PROJECT_TEMPLATE, PROJECT_NAME))