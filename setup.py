import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
  long_description = f.read()

about = {}
with open(os.path.join(here, 'regalias', 'about.py')) as f:
  exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,
    author=about['__author__'],
    author_email='letlafox+pypi@gmail.com',
    url='https://github.com/letla/regalias',
    packages=['regalias'],
    entry_points={
        'console_scripts': ['regalias=regalias.__main__:main'],
    },
    license=about['__license__'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Japanese',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Games/Entertainment :: Role-Playing',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
    ])
