#!/bin/bash

echo "Content-type: text/html"
echo ""

# AWS


echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Hello World</title>'
echo '</head>'
echo '<body>'
echo '<pre>'
echo '<center>'
echo '<bold>'
AWS_PUBLIC_HOSTNAME=$(curl -m 2 http://169.254.169.254/latest/meta-data/public-hostname)
echo "Private Hostname is: $HOSTNAME"
echo
echo "Public Hostname is: $AWS_PUBLIC_HOSTNAME"
# /usr/bin/env
echo '</bold>'
echo '</center>'
echo '</pre>'
echo '</body>'
echo '</html>'
