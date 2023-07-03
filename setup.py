from pathlib import Path
from setuptools import setup, find_packages


setup(
    name='sci',
    version='0.0.1',
    packages=find_packages(),
    install_requires=Path('requirements.txt').read_text().splitlines(),
)
