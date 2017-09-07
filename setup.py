#!/usr/bin/env python

from setuptools import setup
import versioneer


setup(
    name='zish_antlr',
    version=versioneer.get_version(),
    description='A Python 3 library for the Zish format.',
    author='Tony Locke',
    author_email='tlocke@tlocke.org.uk',
    url='https://github.com/tlocke/zish_python_antlr',
    cmdclass=versioneer.get_cmdclass(),
    packages=[
        'zish', 'zish.antlr'],
    install_requires=[
        'antlr4-python3-runtime==4.7',
        'arrow==0.10.0'])
