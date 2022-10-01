from setuptools import setup


setup(
    name='clean_folder',
    version='0.1',
    description='Clean folder',
    url='https://github.com/SSP0d/GoIt_Python_2022/tree/main/autocheck/07/07_homework/clean_folder',
    author='SSP0d',
    author_email='sspod@ukr.net',
    license='MIT',
    install_requires=[],
    packages=['clean_folder'],
    entry_points={
        'console_scripts':
            ['clean-folder = clean_folder.clean:main']
    }
)
