from gettext import find
from importlib.metadata import entry_points
from setuptools import setup, find_packages

__version__ = '0.1.0'

setup(
    name = 'Connect4',
    version = __version__,
    packages = find_packages(include = ['Connect4', 'Connect4Game.src.*'], exclude = ['Connect4Game.test.*']),
    entry_points = {'console_scripts': 'play_game = Connect4.main:main'},
    package_data = {'Connect4': ['config_files/connect4.txt']},
    author = 'Sophia Tierney'
)