#!/usr/bin/python3
""" This script defines a function do_pack """
from fabric.api import local
from datetime import datetime


def do_pack():
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    name = 'web_static_' + date + '.tgz'
    local('mkdir -p versions/')
    descompress = local('tar -zcvf versions/{} web_static'.format(name))
    if descompress.failed:
        return None
    return 'versions/' + name
