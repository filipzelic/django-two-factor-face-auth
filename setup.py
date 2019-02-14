import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-two-factor-face-auth',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Complete Two-Factor Face Authentication for Django',
    long_description=README,
    url='https://github.com/filipzelic/django-two-factor-face-auth',
    author='Filip Zelic',
    author_email='zelic.filip@gmail.com',
    install_requires=[
        'Django>=2.0',
        'Pillow>=2.0',
        'face_recognition>=1.2.3',
        'dlib>=19.7',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
