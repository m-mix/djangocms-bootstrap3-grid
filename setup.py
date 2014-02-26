# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from djangocms_bootstrap3 import __version__


INSTALL_REQUIRES = []

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='djangocms-bootstrap3-grid',
    version=__version__,
    description='Bootstrap3 grid system plugin for django CMS',
    author='Maidakov Mikhail',
    author_email='m-email@inbox.com',
    url='https://github.com/m-mix/djangocms-bootstrap3-grid',
    packages=find_packages(exclude=[]),
    install_requires=INSTALL_REQUIRES,
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False
)
