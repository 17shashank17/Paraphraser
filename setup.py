from setuptools import setup

with open("README.md", "r") as fr:
    long_description = fr.read()

setup(
    name = 'paraphraser',
    version = '0.0.1',
    description = "A python module which returns list of sentences with same contextual meaning as given sentence",
    py_modules = ["paraphraser"],
    package_dir = {'':'src'},
    classifiers = [
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    install_requires = [
        "googletrans ~= 3.0.0",
    ],
    extras_require = {
        "dev": [
            "pytest>=3.7",
        ]
    },
)