#!/usr/bin/python3
""" This script defines a function do_pack """
from fabric.api import local, env


env.hosts = [
    '34.138.131.46',
    '34.228.168.55'
]

env.user = "ubuntu"


def do_pack():
    date = local('date "+%Y%m%d%H%M%S"')
    name = 'web_static_' + date + '.tgz'
    local('mkdir -p versions/')
    local('tar -zcvf versions/{} web_static/'.format(name))
