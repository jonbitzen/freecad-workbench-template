from setuptools import setup
import os

from freecad.my_wb_package.version import __version__

version_path = \
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 
        "freecad", 
        "my_wb_package", 
        "version.py"
    )

with open(version_path) as fp:
    exec(fp.read())

setup(
    name='freecad.model_airplane_design',
    version=str(__version__),
    packages=[
        'freecad',
        'freecad.my_wb_package'
        ],
    maintainer="Your Name",
    maintainer_email="your_name@email_domain.com",
    url="",
    description="workbench to design cool stuff",
    install_requires=[],
    include_package_data=True
)
