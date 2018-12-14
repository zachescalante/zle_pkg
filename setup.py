import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zle_pkg",
    version="0.0.2",
    author="Zachary Escalante",
    author_email="zach.escalante@gmail.com",
    description="This a string formatting package",
    long_description="String formatting for Machine Learning input",
    long_description_content_type="text/markdown",
    url="https://github.com/zachescalante/zle_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)