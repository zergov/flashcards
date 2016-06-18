from setuptools import setup
from setuptools import find_packages

DESCRIPTION = ("CLI application that focus on quickly creating "
               "study flash cards")

REQUIREMENTS = ['click==6.6']

setup(
    name='pyflashcards',
    author='Jonathan Lalande',
    author_email='jonathan.lalande.1@ens.etsmtl.ca',
    version='1.0.2',
    license='MIT',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    data_files=[('/etc/bash_completion.d/', ['flashcards-complete.sh'])],
    entry_points="""
        [console_scripts]
        flashcards=flashcards.main:cli
    """
)
