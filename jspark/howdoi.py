#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Provides Helper Functions while working with Bluemix Spark Notebooks.

This module provides helper functions based on IBM jStart experiences.
More specifically, these functions are oriented towards teaching and
learning example invocations and patterns based on our hours of
experience and web searches in order to make your notebook experience
more efficient.
Enjoy!
"""


def define_filename_swift_url():
    print "# Notice the use of the default account name 'spark'."
    print "filename = 'swift://<bluemix_objstor_containername>.spark/<filename_or_manifest>'"


def read_from_bluemix_spark_service_object_storage():
    define_filename_swift_url()
    print "my_rdd = sc.textFile(filename)"


def persist_my_rdd():
    print "my_rdd = sc.textFile(<filename>).persist(pyspark.storagelevel.StorageLevel.MEMORY_AND_DISK)"


def cleanup_an_rdd_with_errors():
    define_filename_swift_url()
    print "my_rdd = sc.textFile(filename).flatMap(lambda line: cleanup(line)).persist(pyspark.storagelevel.StorageLevel.MEMORY_AND_DISK)"
