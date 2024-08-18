from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "Readme.md").read_text()

setup(
    name='handy_cricket', 
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    author='Ramakrishna Pavan',
    author_email='pavanm630@gmail.com',
    description='A fun, interactive hand cricket game where you can play against the computer.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    project_urls={
        'Source Repository': 'https://github.com/krishnapavan630'
    },
    include_package_data=True,
)
