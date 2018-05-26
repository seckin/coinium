"""
py2app build script for MyApplication.

Will automatically ensure that all build prerequisites are available
via ez_setup.

Usage:
    python setup.py py2app
"""
#import ez_setup
#ez_setup.use_setuptools()

from setuptools import setup
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'coinium.icns'
}
setup(
    app=["graph.py"],
    options={'py2app': OPTIONS},
    setup_requires=["py2app"],
)
