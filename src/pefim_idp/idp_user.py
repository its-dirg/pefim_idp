#from dirg_util.dict import LDAPDict
#ldap_settings = {
#    "ldapuri": "ldaps://ldap.test.umu.se",
#    "base": "dc=umu, dc=se",
#    "filter_pattern": "(uid=%s)",
#    "user": "",
#    "passwd": "",
#    "attr": [
#        "eduPersonScopedAffiliation",
#        "eduPersonAffiliation",
#        "eduPersonPrincipalName",
#        "givenName",
#        "sn",
#        "mail",
#        "uid",
#        "o",
#        "c",
#        "labeledURI",
#        "ou",
#        "displayName",
#        "norEduPersonLIN"
#    ],
#    "keymap": {
#        "mail": "email",
#        "labeledURI": "labeledURL",
#    },
#    "static_values": {
#        "eduPersonTargetedID": "one!for!all",
#    },
#    "exact_match": True,
#    "firstonly_len1": True,
#    "timeout": 15,
#}
#Uncomment to use a LDAP directory instead.
#USERS = LDAPDict(**ldap_settings)

USERS = {
    "testuser": {
            "sn": "Testsson",
            "givenName": "Test",
            "eduPersonAffiliation": "student",
            "eduPersonScopedAffiliation": "student@example.com",
            "eduPersonPrincipalName": "test@example.com",
            "uid": "testuser1",
            "eduPersonTargetedID": "one!for!all",
            "c": "SE",
            "o": "Example Co.",
            "ou": "IT",
            "initials": "P",
            "schacHomeOrganization": "example.com",
            "email": "hans@example.com",
            "displayName": "Test Testsson",
            "labeledURL": "http://www.example.com/haho My homepage",
            "norEduPersonNIN": "SE199012315555",
            "PVP-VERSION": "PVP-VERSION",
            "PVP-PRINCIPAL-NAME": "PVP-PRINCIPAL-NAME",
            "PVP-GIVENNAME": "PVP-GIVENNAME",
            "PVP-BIRTHDATE": "PVP-BIRTHDATE",
            "PVP-USERID": "PVP-USERID",
            "PVP-GID": "PVP-GID",
            "PVP-BPK": "PVP-BPK",
            "PVP-MAIL": "PVP-MAIL",
            "PVP-TEL": "PVP-TEL",
            "PVP-PARTICIPANT-ID": "PVP-PARTICIPANT-ID",
            "PVP-PARTICIPANT-OKZ": "PVP-PARTICIPANT-OKZ",
            "PVP-OU-OKZ": "PVP-OU-OKZ",
            "PVP-OU": "PVP-OU",
            "PVP-OU-GV-OU-ID": "PVP-OU-GV-OU-ID",
            "PVP-FUNCTION": "PVP-FUNCTION",
            "PVP-ROLES": "PVP-ROLES",
            "PVP-INVOICE-RECPT-ID": "PVP-INVOICE-RECPT-ID",
            "PVP-COST-CENTER-ID": "PVP-COST-CENTER-ID",
            "PVP-CHARGE-CODE": "PVP-CHARGE-CODE",
    }
}

EXTRA = {
}