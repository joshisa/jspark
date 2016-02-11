#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Provides Helper Functions while working with Bluemix Spark Notebooks.

This module provides helper functions based on IBM jStart experiences.
Enjoy!
"""


def jstart():
    print "jStart's unique mission within IBM is to leverage emerging technologies to address real and current business needs of our clients.  To check out all of our innovative work and thoughts, please check us out @ http://www-01.ibm.com/software/ebusiness/jstart/about/ and http://blog.ibmjstart.net"


def bluemix():
    print "Vincent Van Gogh once said, 'Great things are done by a series of small things brought together.'  We hope you enjoy your Bluemix Spark Analytics experience."


def reference():
    print "http://docs.openstack.org/developer/swift/api/large_objects.html\n\
           http://spark.apache.org/docs/latest/storage-openstack-swift.html\n\
           https:https://cdsx.ng.bluemix.net/data/jupyter2/d64cf4dc-7ce9-411c-9c9a-3bd0f431a9ad/notebooks/8b4891ab-3cfe-4b6b-872f-8d64c9fd16e0#//spark.apache.org/docs/1.1.1/api/python/pyspark.rdd.RDD-class.html\n\
           https://gist.github.com/dapangmao/5c3798d72b650a70c4bb\n\
           http://www.supergloo.com/fieldnotes/apache-spark-transformations-python-examples/\n\
           https://ogirardot.wordpress.com/2015/05/29/rdds-are-the-new-bytecode-of-apache-spark/\n\
           https://www.dataquest.io/blog/spark-intro/\n\
           https://lab.getbase.com/pandarize-spark-dataframes/\n\
           https://www.safaribooksonline.com/library/view/building-spark-applications/9780134393490/part27.html\n\
           http://stackoverflow.com/questions/28981359/why-do-we-need-to-call-cache-or-persist-on-a-rdd#answer-28984561\n\
           https://forums.databricks.com/questions/271/should-i-always-cache-my-rdds.html\n\
           http://www.mccarroll.net/blog/pyspark2/\n\
           http://stackoverflow.com/questions/33092723/performing-lookup-translation-in-a-spark-rdd-or-data-frame-using-another-rdd-df\n\
           https://github.com/ipython-contrib/IPython-notebook-extensions/wiki/Home-3.x\n\
           http://www.movable-type.co.uk/scripts/latlong.html\n\
           http://hortonworks.com/blog/magellan-geospatial-analytics-in-spark/\n\
           https://github.com/dima42/uber-gps-analysis/\n\
           https://github.com/ipython/ipython/wiki/Cookbook:-Connecting-to-a-remote-kernel-via-ssh"


def install_autotime():
    # Installing the very useful iPython extension autotime (src: https://github.com/cpcloud/ipython-autotime)
    %install_ext https://raw.github.com/cpcloud/ipython-autotime/master/autotime.py
    %load_ext autotime
