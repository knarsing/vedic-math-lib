# setup.py

from setuptools import setup, find_packages

setup(
    name="vedic-math-lib",
    version="0.1.0",
    description="A Python library implementing Vedic Mathematics Sutras",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/vedic-math-lib",
    author="Your Name",
    author_email="youremail@example.com",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
