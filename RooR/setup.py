# setup.py
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='Eurocybersecurite-AI-Cybersecurity',
    version='0.2.1',
    description='AI-powered cybersecurity application by Eurocybersecurite',
    long_description = long_description,
    long_description_content_type="text/markdown",
    author='Eurocybersecurite',
    author_email='mohamed.abdessemed@eurocybersecurite.fr',
    license='MIT',
    packages=find_packages(where='RooR'),
    include_package_data=True,
    install_requires=[
        "flask",
        "transformers",
        "torch",
        "scikit-learn"
    ],
    entry_points={
        'console_scripts': [
            'cybersecurity=main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='cybersecurity, audit, remediation, flask, python',
    python_requires='>=3.11',
)
