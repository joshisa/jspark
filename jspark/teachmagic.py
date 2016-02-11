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


def sample_swift_url():
    print "filename = 'swift://<bluemix_objstor_containername>.spark/<filename or manifest>'"


def sample_textFile():
    print "my_rdd = sc.textFile(<filename>)"


def sample_persist():
    print "my_rdd = sc.textFile(<filename>).persist(pyspark.storagelevel.StorageLevel.MEMORY_AND_DISK)"


def sample_cleanup():
    print "my_rdd = sc.textFile(<filename>).flatMap(lambda line: cleanup(line)).persist(pyspark.storagelevel.StorageLevel.MEMORY_AND_DISK)"
