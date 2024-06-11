from setuptools import setup, find_packages

setup(
    name='albertools',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        "hashlib",
        "ssl",
        "hmac",
        "base64",
        "random",
        "os",
        "uuid",
        "subprocess",
        "platform",
        "json",
        "sys"
    ],
    author='Sky-development',
    author_email='alberlab.team@gmail.com',
    description='Tools module for help developers',
    url='https://github.com/Alberlab-Team/albertools',
)
