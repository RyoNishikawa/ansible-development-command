from setuptools import setup, find_packages

setup(
    name='ansible-develop-command',
    version='0.0.3',
    author='Ryo Nishikawa',
    description='development command for ansible.',
    packages=find_packages(exclude=('test')),
    test_suite='test'
)