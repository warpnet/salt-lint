#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import io
import sys

from setuptools import setup, find_packages


version = "0.0.1"

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

with io.open('README.rst', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = [
    'salt',
    'six',
    'pyyaml',
]

if sys.argv[-1] == 'readme':
    print(readme)
    sys.exit()


setup(
    name='salt-lint',
    version=version,
    description=('A command-line utility that checks for best practices '
                 'in SaltStack.'),
    long_description=readme,
    author='Roald Nefs',
    author_email='info@roaldnefs.com',
    url='https://github.com/roaldnefs/salt-lint',
    packages=find_packages(where='lib'),
    package_dir={'': 'lib'},
    entry_points={
        'console_scripts': [
            'salt-lint = saltlint.__main__:main',
        ]
    },
    include_package_data=True,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    keywords='salt, saltstack, lint',
)
