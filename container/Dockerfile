# FROM registry.redhat.io/rhscl/httpd-24-rhel7
FROM fedora:31
LABEL scollier <scollier@redhat.com>
RUN yum -y install hostname httpd iproute python3-mod_wsgi python3 procps-ng && yum clean all
# RUN mkdir -p /var/www/cgi-bin
# ADD ./test.cgi /var/www/cgi-bin/test.cgi
# ADD ./_htaccess /var/www/cgi-bin/.htaccess
# ADD ./mod_cgid.conf /etc/httpd/conf.modules.d/11-mod_cgid.conf
# RUN chmod +x /var/www/cgi-bin/test.cgi && chown apache.apache /var/www/cgi-bin/test.cgi
CMD [ "/sbin/httpd", "-D", "FOREGROUND" ]

