#!/usr/bin/env python
# -*- coding: utf-8 -*-
from saml2 import BINDING_HTTP_REDIRECT, BINDING_URI
from saml2 import BINDING_HTTP_ARTIFACT
from saml2 import BINDING_HTTP_POST
from saml2 import BINDING_SOAP
from saml2.cert import OpenSSLWrapper
from saml2.saml import NAME_FORMAT_URI
from saml2.saml import NAMEID_FORMAT_TRANSIENT
from saml2.saml import NAMEID_FORMAT_PERSISTENT
import os.path

try:
    from saml2.sigver import get_xmlsec_binary
except ImportError:
    get_xmlsec_binary = None

if get_xmlsec_binary:
    xmlsec_path = get_xmlsec_binary(["/opt/local/bin"])
else:
    xmlsec_path = '/usr/bin/xmlsec1'

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def verify_encrypt_cert(cert_str):
    osw = OpenSSLWrapper()
    ca_cert_str = osw.read_str_from_file("/Users/haho0032/Develop/root_cert/localhost.ca.crt")
    valid, mess = osw.verify(ca_cert_str, cert_str)
    return valid


def full_path(local_file):
    return os.path.join(BASEDIR, local_file)


#If HTTPS is true you have to assign the server cert, key and certificate chain.
HTTPS = True
SERVER_CERT = "httpsCert/localhost.crt"
SERVER_KEY = "httpsCert/localhost.key"
#CERT_CHAIN="certs/chain.pem"
CERT_CHAIN = None

HOST = 'localhost'
PORT = 8078

BASE = "https://%s:%s" % (HOST, PORT)

CONFIG = {
    "entityid": "%s/TestIdP.xml" % BASE,
    "description": "TestIDP",
    "valid_for": 168,
    "service": {
        "aa": {
            "endpoints": {
                "attribute_service": [
                    ("%s/attr" % BASE, BINDING_SOAP)
                ]
            },
            "name_id_format": [NAMEID_FORMAT_TRANSIENT,
                               NAMEID_FORMAT_PERSISTENT]
        },
        "aq": {
            "endpoints": {
                "authn_query_service": [
                    ("%s/aqs" % BASE, BINDING_SOAP)
                ]
            },
        },
        "idp": {
            "name": "TestIdP",
            "want_authn_requests_signed": True,
            "want_authn_requests_only_with_valid_cert": True,
            "sign_response": True,
            "sign_assertion": False,
            "verify_encrypt_cert": verify_encrypt_cert,
            "encrypt_assertion": True,
            "endpoints": {
                "single_sign_on_service": [
                    ("%s/sso/redirect" % BASE, BINDING_HTTP_REDIRECT),
                    ("%s/sso/post" % BASE, BINDING_HTTP_POST),
                    ("%s/sso/art" % BASE, BINDING_HTTP_ARTIFACT),
                    ("%s/sso/ecp" % BASE, BINDING_SOAP)
                ],
                "single_logout_service": [
                    ("%s/slo/soap" % BASE, BINDING_SOAP),
                    ("%s/slo/post" % BASE, BINDING_HTTP_POST),
                    ("%s/slo/redirect" % BASE, BINDING_HTTP_REDIRECT)
                ],
                "artifact_resolve_service": [
                    ("%s/ars" % BASE, BINDING_SOAP)
                ],
                "assertion_id_request_service": [
                    ("%s/airs" % BASE, BINDING_URI)
                ],
                "manage_name_id_service": [
                    ("%s/mni/soap" % BASE, BINDING_SOAP),
                    ("%s/mni/post" % BASE, BINDING_HTTP_POST),
                    ("%s/mni/redirect" % BASE, BINDING_HTTP_REDIRECT),
                    ("%s/mni/art" % BASE, BINDING_HTTP_ARTIFACT)
                ],
                "name_id_mapping_service": [
                    ("%s/nim" % BASE, BINDING_SOAP),
                ],
            },
            "policy": {
                "default": {
                    "lifetime": {"minutes": 15},
                    #"attribute_restrictions": None, # means all I have
                    "name_form": NAME_FORMAT_URI,
                    "entity_categories": ["at_egov_pvp2"]
                },
            },
            "subject_data": "./idp.subject",
            "name_id_format": [NAMEID_FORMAT_TRANSIENT,
                               NAMEID_FORMAT_PERSISTENT]
        },
    },
    "debug": 1,
    "key_file": full_path("pki/mykey.pem"),
    "cert_file": full_path("pki/mycert.pem"),
    "metadata": {
        "local": ["/Users/haho0032/Develop/githubFork/pysaml2/example/sp-repoze/sp.xml",
                  "/Users/haho0032/Develop/github/pefim-proxy/example/pefim_proxy_conf.xml"],
    },
    "organization": {
        "display_name": "Test IdP",
        "name": "Test IdP",
        "url": "http://localhost:8737",
    },
    "contact_person": [
        {
            "contact_type": "technical",
            "given_name": "Test",
            "sur_name": "Testsson",
            "email_address": "test.testssong@test.se"
        },
    ],
    # This database holds the map between a subjects local identifier and
    # the identifier returned to a SP
    "xmlsec_binary": xmlsec_path,
    #"attribute_map_dir": "../attributemaps",
    "logger": {
        "rotating": {
            "filename": "idp.log",
            "maxBytes": 500000,
            "backupCount": 5,
        },
        "loglevel": "debug",
    }
}
