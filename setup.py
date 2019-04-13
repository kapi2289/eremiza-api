import io
import re
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with io.open(path.join(here, "eremiza/__init__.py"), "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

setup(
    name="eremiza-api",
    version=version,
    packages=["eremiza"],
    author="Kacper Ziubryniewicz",
    author_email="kapi2289@gmail.com",
    license="MIT",
    install_requires=["requests", "PyJWT"],
)
