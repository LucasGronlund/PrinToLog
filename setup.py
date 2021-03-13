import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='printolog',
    version='0.1',
    description='Python decorator that makes functions use a logger instead of print.',
    long_description=README,
    long_description_content_type="text/markdown",
    packages=['printolog'],
    license='MIT',
    author='Lucas Grönlund',
    author_email='lucasgronlund@gmail.com',
    url='https://github.com/LucasGronlund/PrinToLog',
    keywords=['logging', 'decorator', 'print'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
