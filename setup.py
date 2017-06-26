import os

from setuptools import setup
from setuptools.command.test import test as TestCommand


install_requires = [
    'requests',
    'termcolor',
    'packaging',
]
tests_require = install_requires + [
    'pytest==3.1.2',
    'tox==2.7.0',
    'mock==2.0.0',
]
release_require = [
    'zest.releaser==6.12',
    'twine>=1.9.1,<2.0',
]


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


class PyTest(TestCommand):
    user_options = []

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, '-m', 'pytest', 'tests'])
        raise SystemExit(errno)


args = dict(
    name='leak',
    version='1.1.0',
    description='Show available releases for package',
    long_description=read('README.rst'),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Version Control',
        'Topic :: Utilities',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        ],
    author='Misha Behersky',
    author_email='bmwant@gmail.com',
    url='http://bmwlog.pp.ua',
    license='MIT License',
    packages=['leak'],
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'dev': tests_require + release_require
    },
    scripts=['scripts/leak'],
    include_package_data=True,
    cmdclass=dict(test=PyTest)
)

setup(**args)
