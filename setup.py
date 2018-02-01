#!/usr/bin/env python
# coding: utf-8

from distutils.core import setup

for cmd in ('egg_info', 'develop'):
    import sys
    if cmd in sys.argv:
        from setuptools import setup

import sys

is_py2 = sys.version_info < (3, 0, 0)

if is_py2:
    reload(sys).setdefaultencoding("UTF-8")

setup(
    name='django-paymaster',
    version='0.2.0',
    author='Ivan Petuhov',
    author_email='satels@gmail.com',

    include_package_data=True,
    packages=['paymaster'],
    package_data={
        'paymaster': ['migrations/*.py', 'templates/paymaster/*.html']
    },

    url='https://github.com/satels/django-paymaster/',
    download_url='https://github.com/satels/django-paymaster/zipball/master',
    license='MIT license',
    description=('Application for integration PayMaster payment '
                 'system in Django projects.').encode('utf8'),
    long_description=(
        'Приложение для интеграции платежной системы PayMaster '
        '(http://paymaster.ru/) в проекты на Django. Реализовано '
        'только основное API PayMaster, согласно спецификации'
        'http://paymaster.ru/Partners/ru/docs/protocol/\n\n'
        'С ознакомиться документацией, а так же сообщить об '
        'ошибках можно на странице проекта '
        'http://github.com/scailer/django-paymaster/'
    ).encode('utf8'),

    requires=['django (>= 1.5)', 'pytz', 'simple_crypt'],

    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
