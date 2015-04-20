# coding=utf-8
from setuptools import setup

setup(
    name="pefim_idp",
    version="0.1",
    description='SAML IdP for the pefim profile.',
    author="Mathias Hedström",
    author_email="mathias.hedstrom@umu.se",
    license="Apache 2.0",
    packages=["pefim_idp"],
    package_dir={"": "src"},
    classifiers=["Development Status :: 0.1 - Beta",
                 "License :: OSI Approved :: Apache Software License",
                 "Topic :: Software Development :: Libraries :: Python Modules"],
    install_requires=["mako"], #, "pysaml2"
    entry_points={
        'console_scripts': ['pefim_idp=pefim_idp.server:main'],
    },
    zip_safe=False
)
