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
APP_NAME = "Coinium"
OPTIONS = {
    'argv_emulation': True,
    'iconfile': '/Users/seckin/coinium/admin/coinium',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Coinium Portfolio Management",
        'CFBundleIdentifier': "app.coinium.osx.coinium",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Copyright © 2018, Seckin Can Sahin, All Rights Reserved"
    },
    'includes': 'wx.adv,wx.html,wx.xml'
}
setup(
    app=["obfuscated_graph.py"],
    options={'py2app': OPTIONS},
    setup_requires=["py2app"],
)
