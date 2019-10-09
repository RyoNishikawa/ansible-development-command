from setuptools import setup, find_packages

setup(
    name='ansible-development-command',
    version='0.3.0',
    author='Ryo Nishikawa',
    author_email='ryo.pg.se@gmail.com',
    url='https://github.com/RyoNishikawa/',
    description='development command for ansible.',
    package_dir={'': 'lib'},
    packages=find_packages('lib'),
    #packages=['adc'],
    scripts=['bin/adc'],
    test_suite='test'
)
