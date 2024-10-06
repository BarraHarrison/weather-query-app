from setuptools import setup, find_packages

setup(
    name='my_package',  
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'spacy',
        'python-dotenv',
        'dateparser',
    ],
    entry_points={
        'console_scripts': [
            'weather-cli=my_package.cli:main',
        ],
    },
    include_package_data=True,
    description='A package to answer natural language weather questions.',
    author='Your Name',
    author_email='your.email@example.com',
)
