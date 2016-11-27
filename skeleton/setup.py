
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Grzegorz Basta',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'grzegorz.bas04@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
