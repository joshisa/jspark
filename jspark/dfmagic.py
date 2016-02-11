#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Provides Helper Functions while working with Bluemix Spark Notebooks.

This module provides helper functions based on IBM jStart experiences.
More specifically, these functions are oriented towards Spark
Dataframes.
Enjoy!
"""


# https://lab.getbase.com/pandarize-spark-dataframes/
def addEmptyColumns(df, colNames):
    exprs = df.columns + ["null as " + colName for colName in colNames]
    return df.selectExpr(*exprs)


def concatTwoDfs(left, right):
    # append columns from right df to left df
    missingColumnsLeft = set(right.columns) - set(left.columns)
    left = addEmptyColumns(left, missingColumnsLeft)

    # append columns from left df to right df
    missingColumnsRight = set(left.columns) - set(right.columns)
    right = addEmptyColumns(right, missingColumnsRight)

    # let's set the same order of columns
    right = right[left.columns]

    # finally, union them
    return left.unionAll(right)


def concat(dfs):
    return reduce(concatTwoDfs, dfs)
