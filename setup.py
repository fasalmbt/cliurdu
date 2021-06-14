from setuptools import setup

def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()

setup(
    name="cliurdu",
    version="1.0.0",
    description="A simple cli based utility for urdu dictionary",
    long_description=readfile('README.md'),
    license=readfile('LICENSE'),
    url="https://github.com/fasalmbt/cliurdu",
    py_modules=['cliurdu'],
    entry_points={
        'console_scripts': [
            'cliurdu = cliurdu:main'
        ]
    },
)