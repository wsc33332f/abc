from setuptools import setup, find_packages

setup(
    name="abc-library",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Hikauiro",
    author_email="email@example.com",
    description="A simple Python library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wsc33332f/abc",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
