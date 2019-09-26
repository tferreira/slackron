import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

_TEST_REQUIRE = [
    "pylint==2.4.1"
]

setuptools.setup(
    name="slackron",
    version="0.0.4",
    author="Thomas Ferreira",
    author_email="fulura@gmail.com",
    description="A Python wrapper to notify about cronjob execution to Slack",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tferreira/slackron",
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=[
        "PyYAML==5.1.2",
        "requests==2.22.0"
    ],
    tests_require=_TEST_REQUIRE,
    extras_require={"testing": _TEST_REQUIRE},
    entry_points = {
        'console_scripts': ['slackron=slackron.__init__:run'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
