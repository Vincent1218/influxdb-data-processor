from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A data processor for data in influxDB'

# Setting up
setup(
    name="influxdb-data-processor",
    version=VERSION,
    author="Pikacent (Chai Wen Xuan)",
    author_email="<vicentchai@hotmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['influxdb_client','pandas','numpy','scipy'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)