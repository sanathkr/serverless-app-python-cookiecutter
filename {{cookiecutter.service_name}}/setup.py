#!/usr/bin/env python

import io
import re
import os
from setuptools import setup, find_packages

module_name = "{{cookiecutter.package_name}}"

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', os.linesep)
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


def read_requirements(req='base.txt'):
    content = read(req)
    return [line for line in content.split(os.linesep)
            if not line.strip().startswith('#')]


def read_all_requirements(folder, reqname="requirements.txt"):
    requirements = []

    for root, dirs, files in os.walk(folder):
        if reqname in files:
            requirements += read_requirements(os.path.join(root, reqname))

    return requirements


def read_version():
    content = read(os.path.join(
        os.path.dirname(__file__), '{{cookiecutter.package_name}}', '__init__.py'))
    return re.search(r"__version__ = '([^']+)'", content).group(1)


setup(
    name='{{cookiecutter.package_name}}',
    version=read_version(),
    description='{{cookiecutter.service_name}} Service',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author}}',
    url='{{cookiecutter.repo_url}}',
    license='Apache License 2.0',
    packages=find_packages(exclude=['tests.*', 'tests']),
    keywords="{{cookiecutter.service_name}} Service",
    # Support Python 2.7 and 3.6 or greater
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
    install_requires=read_all_requirements(module_name, reqname="requirements.txt"),
    extras_require={
        'dev': read_requirements('requirements-dev.txt')
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Utilities',
    ]
)
