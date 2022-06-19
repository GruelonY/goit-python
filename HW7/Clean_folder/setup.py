from setuptools import setup, find_packages

setup(
    name='Sorting files',
    version='1.0.0',
    description='Sorting your file',
    url='https://github.com/GruelonY/goit-python/tree/main',
    author='Dmytro Babenko',
    author_email='babenko1656@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)