import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slackron",
    version="0.0.1",
    author="Thomas Ferreira",
    author_email="fulura@gmail.com",
    description="A Python wrapper to notify about cronjob execution to Slack",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tferreira/slackron",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests==2.22.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
