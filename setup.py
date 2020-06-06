from setuptools import setup, find_packages

setup(
    name='rapid',
    version='1.0',
    py_modules=['rapid'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        rapid=rapid.cli:start
    ''',
)
