#!/bin/bash

cat <<EOF

Generating a new test key and certificate.  To change the defaults offered
by openssl, edit your openssl.cnf, such as /etc/ssl/openssl.cnf

EOF

openssl genrsa -out server.key 1024
chmod 600 server.key
openssl req -new -key server.key -out server.csr
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

cat <<EOH

Now to enable these new keys, do:

  cp server.key pki/mykey.pem
  cp server.crt pki/mycert.pem

  cp server.key pki/mykey.pem
  cp server.crt pki/mycert.pem

EOH
