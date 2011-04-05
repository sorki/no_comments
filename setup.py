from distutils.core import setup
import os

NAME = 'no_comments'
VERSION = '0.1'

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read().strip()
f.close()

setup(name=NAME,
        version=VERSION,
        description='no_comments strips comments from various file types',
        long_description=long_description,
        author='Richard Marko',
        author_email='rissko@gmail.com',
        url='http://github.com/sorki/no_comments',
        license='BSD',
        scripts=['src/no_comments'],

        classifiers=['Development Status :: 4 - Beta',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Text Processing :: Filters']
    )
