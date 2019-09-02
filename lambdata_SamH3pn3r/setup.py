"""

lambdata - a collection of DS helper functions

"""

import setuptools

REQUIRED = [
    "numpy",
    "pandas",
    "matplotlib",
    "scikit-learn"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="lambdata-sam",
    version="0.0.1",
    author="SamH3pn3r",
    description="A collection of DS helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/SamH3pn3r/lambdata-sam",
    packages=setuptools.findpackages(),
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)    