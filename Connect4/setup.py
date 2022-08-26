from setuptools import setup, find_packages

__version__ = '0.1.0' # major version - 0, minor version - 1, maintenance version - 0

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name='connect4-app',
    author='Sophia Tierney',
    version=__version__,
    author_email='sftierney@ucdavis.edu',
    description='A command line implementation of the classic Connect4 game written in pure Python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/soph-py/connect4_app',
    keywords='python, docker, cli-app, oop, connect4',
    packages=find_packages(
        include = ['Connect4', 'Connect4Game.src.*'], 
        exclude = ['Connect4Game.test.*']
        ),
    entry_points={
        'console_scripts': 'play_game = Connect4.main:main'
        },
    package_data={
        'Connect4': ['config_files/connect4.txt']
        },
    include_package_data=True,
    python_requires='>=3.5',
    classifiers=[
        'Topic :: Games/Entertainment :: Board Games',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ]
)