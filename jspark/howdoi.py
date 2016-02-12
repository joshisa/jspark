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


def install_autotime_extension():
    print "This extension allows you to automatically time every cell"
    print "After a cell is executed, you will see a timing value output"
    print "This is useful in identifying slow running cells"
    print ""
    print "No. of Cells to execute: 1"
    print "--------------------------"
    print ""
    print "Cell 1 - Paste text below"
    print "# Installing the very useful iPython extension autotime"
    print "%install_ext https://raw.github.com/cpcloud/ipython-autotime/master/autotime.py"
    print "%load_ext autotime"
    print ""
    print "Test: verify the presence of a time value output generation following cell execution"
    print "See https://github.com/cpcloud/ipython-autotime for more details"


def install_codefolding_extension():
    print "This extension adds codefolding functionality from CodeMirror to a codecell."
    print "After clicking on the gutter or typing Alt+F, the code gets folded."
    print "This is useful in reducing visual noise of your notebook"
    print ""
    print "No. of Cells to execute: 3"
    print "--------------------------"
    print ""
    print "Cell 1 - Paste text below"
    print "# Install Notify Jupyter nbextension"
    print "import IPython.html.nbextensions as nb"
    print "ext= 'https://github.com/ipython-contrib/IPython-notebook-extensions/archive/3.x.zip'"
    print "nb.install_nbextension(ext, user=True)"
    print ""
    print "Cell 2 - Paste text below"
    print "%%javascript"
    print "IPython.load_extensions('IPython-notebook-extensions-3.x/usability/codefolding/main');"
    print ""
    print "Cell 3 - Paste text below"
    print "# Activate codefolding extension"
    print "from IPython.html.services.config import ConfigManager"
    print "ip = get_ipython()"
    print "cm = ConfigManager(parent=ip, profile_dir=ip.profile_dir.location)"
    print "cm.update('notebook', {'load_extensions': {'IPython-notebook-extensions-3.x/usability/codefolding/main': True}})"
    print ""
    print "Test:  Both Cell 1 and Cell 3 should now show a clickable triangle next to the cell's first line which is a comment"
    print "See https://github.com/ipython-contrib/IPython-notebook-extensions/wiki/Codefolding for more details."


def declare_dataframe_schema():
    print "# Establishing sqlContext and schema for dataframe creation "
    print "sqlContext = SQLContext(sc)"
    print "schema = StructType(["
    print "     StructField( header_list[0], ArrayType(ArrayType(DoubleType())), False),"
    print "     StructField( header_list[1], DoubleType(), False),"
    print "     StructField( header_list[2], StringType(), False),"
    print "     StructField( header_list[3], StringType(), False),"
    print "     StructField( header_list[4], StringType(), False)"
    print "])"
    print ""
    print "df = sqlContext.createDataFrame(my_rdd, schema).persist(pyspark.storagelevel.StorageLevel.MEMORY_AND_DISK)"
