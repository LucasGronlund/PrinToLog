from setuptools import setup

setup(
    name='printolog',
    version='0.1',
    description='Python decorator that makes functions use a logger instead of print.',
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
