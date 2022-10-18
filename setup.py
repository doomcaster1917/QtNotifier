from setuptools import setup, find_packages

long_description = open('README.md').read()

DESCRIPTION = 'Бот для партии'
LONG_DESC = long_description

setup(
    name='QtNotifier',
    version='1.0.0',
    author='doomcaster1917',
    author_email='webtalestoday@gmail.com',
    url='https://github.com/doomcaster1917/QtNotifier',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    long_description=LONG_DESC,
    
    install_requires=[
        'vk_api',
        'PyQt6',
        'SQLAlchemy'
    ]
)
