from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tagalog_number",
    version="1.0.0",
    author="Brian Balili",
    author_email="brian.balili3@gmail.com",
    description="A package to convert numbers to Tagalog words and vice versa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eautify/tagalog-number-converter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='tagalog number converter filipino',
    project_urls={
        'Source': 'https://github.com/eautify/tagalog-number-converter',
        'Bug Reports': 'https://github.com/eautify/tagalog-number-converter/issues',
    },
)