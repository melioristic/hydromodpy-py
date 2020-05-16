import setuptools

with open("README.md","r") as fh:
    long_description  = fh.read()

setuptools.setup(
    name = "hydromodpy-meliorist",
    version = "0.0.1",
    author="Mohit Anand",
    author_email = "itsmohitanand@gmail.com",
    description = "A package for hydrological modelling",
    long_description = long_description,
    url = "https://github.com/melioristic/hydromodpy",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent"
    ],
    python_requires = ">=3.6",
)
