#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Provides Helper Functions while working with Bluemix Spark Notebooks.

This module provides helper functions based on IBM jStart experiences.
More specifically, these functions are oriented towards basic
operations and interaction typically encountered in notebook workloads
Enjoy!
"""

from IPython.display import Audio
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, ArrayType, DoubleType, StringType, FloatType, IntegerType
from pyspark.storagelevel import StorageLevel
from pyspark.accumulators import AccumulatorParam
import os
import twilio
import twilio.rest


DEFAULT_MESSAGE = "Vincent Van Gogh once said, 'Great things are done by a "\
                  "series of small things brought together.' Your IPython "\
                  "cell has completed."
DEFAULT_MODE = "audio"
notify_sound = "https://ibm.box.com/shared/static/r50psi487u4x4jfo7ejlhqnaozska5bp.ogg"
credentials = {
    "auth_url": "https://identity.open.softlayer.com",
    "project": "",
    "projectId": "",
    "region": "dallas",
    "userId": "",
    "username": "",
    "password": "",
    "domainId": "",
    "domainName": "",
    "name": "",
    "container": "",
    "twilio_account_sid": "",
    "twilio_auth_token": "",
    "twilio_to_number": "",
    "twilio_from_number": ""
}


def jstart():
    print "jStart's unique mission within IBM is to leverage emerging technologies " \
          "to address real and current business needs of our clients.  To check " \
          "out all of our innovative work and thoughts, please check us out @ " \
          "http://www-01.ibm.com/software/ebusiness/jstart/about/ and " \
          "http://blog.ibmjstart.net"


def bluemix():
    print "Vincent Van Gogh once said, 'Great things are done by a series of " \
          "small things brought together.'  We hope you enjoy your Bluemix " \
          "Spark Analytics experience."


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


def install(package):
    os.system("pip install --user " + package + " > /dev/null 2>&1")


def sms(smsbody=DEFAULT_MESSAGE):
    try:
        client = twilio.rest.TwilioRestClient(credentials["twilio_account_sid"],
                                              credentials["twilio_auth_token"])
        client.messages.create(
            body=smsbody,
            to=credentials["twilio_to_number"],
            from_=credentials["twilio_from_number"]
        )
        return "success"
    except twilio.TwilioRestException as e:
        return e


# Let's setup alerting capabilities to make long-running cells tolerable
def notify(mode=DEFAULT_MODE, message=DEFAULT_MESSAGE):
    if mode == "sms":
        if (len(message) > 0):
            sms(message)
        else:
            sms()
        return "IPython Cell Complete SMS sent to %s" % \
               credentials['twilio_to_number']
    elif mode == "mixed":
        if (len(message) > 0):
            sms(message)
        else:
            sms()
        return Audio(url=notify_sound, autoplay=True)
    elif mode == "audio":
        return Audio(url=notify_sound, autoplay=True)
    else:
        return Audio(url=notify_sound, autoplay=True)


def uni_to_int(uni):
    num = None
    try:
        num = int(uni)
    except:
        pass
    return num
