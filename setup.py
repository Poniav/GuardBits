# ===========================================================================
# Guard Application 
# ===========================================================================

import pathlib
import sys
from os import path

from setuptools import find_packages, setup

min_version = (3, 6)

here = pathlib.Path(__file__).parent.absolute()
print(here)

with open('README.rst') as readme_file:
    readme = readme_file.read()
#with open(here / 'README.rst', encoding='utf-8') as readme_file:
#    readme = readme_file.read()


#with open(here / 'requirements.txt', 'rt') as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
#    requirements = [line for line in requirements_file.read().splitlines()
#                    if not line.startswith('#')]

with open('requirements.txt') as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]

setup(
    name='GuardBits',
    license='GNU AGPLv3',
    email='guigarciafr@gmail.com',
    author='Guillaume Garcia',
    packages=['GuardBits', 
              'GuardBits/ressources',
              'GuardBits/files',
              'GuardBits/src',
              'GuardBits/tests'],
    description='Guard application to store confidential datas',
    long_description=readme,
    url='https://github.com/Poniav/GuardBits.git',
    entry_points={
        'console_scripts': [
            # 'some.module:some_function',
        ],
    },
    include_package_data=True,
    # package_data={
    #     'GuardBits': [
    #         # When adding files here, remember to update MANIFEST.in as well,
    #         # or else they will not be included in the distribution on PyPI!
    #         'GuardBits/json/DefaultStyle.json',
    #     ]
    # },
    install_requires=requirements,
    classifiers=[
        'Development Status :: 1 - Prototype',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
