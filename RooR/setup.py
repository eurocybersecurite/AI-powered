# setup.py
from setuptools import setup, find_packages

setup(
    name='Eurocybersecurite-AI-Cybersecurity',
    version='0.1.0',
    description='AI-powered cybersecurity application by Eurocybersecurite',
    author='Eurocybersecurite',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'cybersecurity=main:main',
        ],
    },
)
