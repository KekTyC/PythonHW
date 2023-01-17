from setuptools import setup, find_packages

setup(
    name='homeproject',
    version='0.1',
    author='Egor Ershov',
    packages=find_packages(),
    install_requires=['pandas', 'argparse'],
    entry_points={
        'console_scripts': [
            'homeproject = homeproject.main:main',
        ],
    }
)