import os
from setuptools import setup, Extension
from glob import glob

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join("../", fname)).read()

setup(
    name = "superdog",
    version = "0.1.1",
    author = "Choonho Son",
    author_email = "choonho.son@gmail.com",
    description = ("Intelligent Chat Bot based on Slack"),
    license = "BSD",
    keywords = "chatbot slack",
    url = "https://github.com/pyengine/superdog",
    packages=['superdog','superdog.plugins', ],
    long_description=read('README.md'),
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    zip_safe=True,
    install_requires=['slackclient'],
    entry_points = {
        'console_scripts': [
            'superdog = superdog.do:main',
            ],
        },
    data_files = [
                ],
)

