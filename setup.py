#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

from auto_deprecator_example import __version__

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'auto-deprecator',
    'docopt',
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Gavin Chan",
    author_email='gavincyi at gmail dot com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Auto deprecator example",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='auto_deprecator_example',
    name='auto_deprecator_example',
    packages=find_packages(include=['auto_deprecator_example', 'auto_deprecator_example.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/gavincyi/auto_deprecator_example',
    version=__version__,
    zip_safe=False,
    entry_points="""
        [console_scripts]
        hello-world-app = auto_deprecator_example.cli.hello_world_app:main
    """,
)
