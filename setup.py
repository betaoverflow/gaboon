import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gaboon",
    version="0.1",
    author="Aniket Pal",
    author_email="aniketindian8@gmail.com",
    description="A collection of Algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['gaboon'],
    url="https://github.com/betaoverflow/gaboon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
