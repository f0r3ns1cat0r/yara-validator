from distutils.core import setup

setup(
    name = 'yara_validator',
    packages = ['yara_validator'],
    version = '0.1',  # Ideally should be same as your GitHub release tag varsion
    description = 'A simple library to check yara rules syntax',
    author = 'CIRCL - edhoedt',
    author_email = 'edhoedt@gmail.com',
    url = 'https://github.com/CIRCL/yara-validator',
    download_url = 'https://github.com/CIRCL/yara-validator/archive/v0.1.tar.gz',
    keywords = ['yara'],
    classifiers = [],
)
