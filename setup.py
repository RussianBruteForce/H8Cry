from setuptools import setup, find_packages

setup (
       name='H8Cry',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['pyqt5>=5.4'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='Viktor Filinkov',
       author_email='bruteforce@sigil.tk',

       summary = 'PyQt5 desktop alarm',
       #url='',
       license='GPLv3',
       long_description='Long description of the package',

       # could also include long_description, download_url, classifiers, etc.

  
       )