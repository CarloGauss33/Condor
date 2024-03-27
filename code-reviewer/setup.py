from setuptools import setup, find_packages

setup(
    name='condor_code_reviewer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'PyGithub',
    ],
    entry_points={
        'console_scripts': [
            'condor=src.cli:main',
        ],
    },
)
