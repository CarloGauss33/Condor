from setuptools import setup, find_packages

setup(
    name='code_reviewer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'PyGithub',
    ],
    entry_points={
        'console_scripts': [
            'review_pull_request=src.cli:main',
        ],
    },
)
