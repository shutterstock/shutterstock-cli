# -*- coding: utf-8 -*-

import os
import sys
from shutil import rmtree

from setuptools import setup, Command

with open("README.md", "rb") as input_file:
    long_descr = input_file.read().decode("utf-8")

HERE = os.path.abspath(os.path.dirname(__file__))

version_ns = {}

with open(os.path.join(HERE, "shutterstock", "__version__.py")) as input_file:
    exec(input_file.read(), {}, version_ns)


class PublishCommand(Command):
    """Support setup.py publish."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(HERE, "dist"))
        except:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPi via Twine…")
        os.system(
            f'twine upload dist/* -u __token__ -p {os.getenv("PYPI_TOKEN")}'
        )

        sys.exit()


setup(
    name="shutterstock-cli",
    packages=["shutterstock", "shutterstock.utils"],
    entry_points={"console_scripts": ["shutterstock = shutterstock.cli:cli"]},
    version=version_ns["__version__"],
    keywords=["shutterstock", "api", "images", "videos", "audio"],
    description="A command-line utility that allows you to interact with the Shutterstock public API.",
    long_description=long_descr,
    long_description_content_type = "text/markdown",
    author="Shutterstock",
    author_email="tech.api.team@shutterstock.com",
    url="https://github.com/shutterstock/shutterstock-cli",
    install_requires=[
        "requests",
        "click",
        "pygments",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    cmdclass={
        "publish": PublishCommand,
    },
)
