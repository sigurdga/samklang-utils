#!/usr/bin/env python
from distutils.core import setup

setup(
        name='samklang-utils',
        version="0.3.4",
        author='Sigurd Gartmann',
        author_email='sigurdga-samklang@sigurdga.no',
        url='http://github.com/sigurdga/samklang-utils',
        description='Common utilities for Samklang',
        long_description=open('README.txt').read(),
        license="AGPL",
        packages = ['samklang_utils', 'samklang_utils.middleware'],
        package_data = {'samklang_utils': ['templates/samklang_utils/*.html', 'static/js/*.js', 'static/css/*.css', 'static/img/*.png', 'locale/*/LC_MESSAGES/django.*o'] },
        install_requires=['django-floppyforms>=0.4.7'],
        classifiers=[
                "Development Status :: 3 - Alpha",
                "License :: OSI Approved :: GNU Affero General Public License v3",
                "Intended Audience :: Developers",
                "Framework :: Django",
                "Environment :: Web Environment",
                "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
                ]
        )

