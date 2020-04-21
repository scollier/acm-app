#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Hello World</title>'
echo '</head>'
echo '<body>'
echo '<pre>'
echo '<center>'
echo '<b>'
echo

# Check for AWS
if [ -f /sys/hypervisor/uuid ] && [ `head -c 3 /sys/hypervisor/uuid` == ec2 ]; then
    echo "This is a host on AWS"
fi

echo '</b>'
echo '</center>'
echo '</pre>'
echo '</body>'
echo '</html>'
