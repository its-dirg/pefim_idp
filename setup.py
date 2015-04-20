#!/usr/bin/env python

import sys

from setuptools import setup

install_requires = [
    # core dependencies
    'pysaml2',
    'mako',
]

# only for Python 2.6
if sys.version_info < (2, 7):
    install_requires.append('importlib')

setup(
    name='pefim_idp',
    version='0.0.1',
    description='idp',
    # long_description = read("README"),
    author='Roland Hedberg',
    author_email='roland.hedberg@adm.umu.se',
    license='',
    url='https://github.com/its-dirg/pefim_idp',

    packages=['saml2', 'xmldsig', 'xmlenc', 's2repoze', 's2repoze.plugins',
              "saml2/profile", "saml2/schema", "saml2/extension",
              "saml2/attributemaps", "saml2/authn_context",
              "saml2/entity_category", "saml2/userinfo"],

    package_data={'': ['xml/*.xml']},

    #scripts=["tools/parse_xsd2.py", "tools/make_metadata.py",
    #         "tools/mdexport.py", "tools/merge_metadata.py"],

    install_requires=install_requires,
    zip_safe=False,
)
