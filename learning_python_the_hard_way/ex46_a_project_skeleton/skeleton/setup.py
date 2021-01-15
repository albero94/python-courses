try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "My Project",
    "author": "Alvaro Albero",
    "url": "https://alvaroalbero.com",
    "download_url": "",
    "author_email": "ealbero94@gmail.com",
    "version": "0.1",
    "install_requieres": ["nose"],
    "packages": ["NAME"],
    "scripts": [],
    "name": "projectname"
}

setup(**config)