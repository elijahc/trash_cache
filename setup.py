from setuptools import setup, find_packages
import trash_cache

# Add setuptools boilerplate
setup(
    name='trash_cache',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=trash_cache.__version__,

    description='trashpandas data storage',
    long_description='trashpandas data storage',

    # The project's main homepage.
    url='https://github.com/elijahc/trash_cache',

    # Author details
    author='Elijah Christensen',
    author_email='ejd.christensen@gmail.com',

    # Choose your license
    license='MIT',
    packages=find_packages()
)