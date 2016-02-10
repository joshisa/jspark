#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Provides Helper Functions while working with Bluemix Spark Notebooks.

This module provides helper functions based on IBM jStart experiences.
More specifically, these functions are oriented towards Bluemix Object
Storage connectivity and interaction.
Enjoy!
"""

import requests
import StringIO
import json


def get_file_content(credentials):
    '''For given credentials, this functions returns a StringIO object containg the file content.'''
 
    url1 = ''.join([credentials['auth_url'], '/v3/auth/tokens'])
    data = {'auth': {'identity': {'methods': ['password'],
            'password': {'user': {'name': credentials['username'], 'domain': {'id': credentials['domainId']},
            'password': credentials['password']}}}}}
    headers1 = {'Content-Type': 'application/json'}
    resp1 = requests.post(url=url1, data=json.dumps(data), headers=headers1)
    resp1_body = resp1.json()   
    for e1 in resp1_body['token']['catalog']:
        if(e1['type'] == 'object-store'):
            for e2 in e1['endpoints']:
                if(e2['interface'] == 'public'and e2['region'] == credentials['region']):
                    url2 = ''.join([e2['url'], '/', credentials['container'], '/', credentials['filename']])
    s_subject_token = resp1.headers['x-subject-token']
    headers2 = {'X-Auth-Token': s_subject_token, 'accept': 'application/json'}
    resp2 = requests.get(url=url2, headers=headers2)
    return StringIO.StringIO(resp2.content)


def set_hadoop_config(sc, credentials):
    prefix = "fs.swift.service." + credentials['name'] 
    hconf = sc._jsc.hadoopConfiguration()
    hconf.set(prefix + ".auth.url", credentials['auth_url']+'/v3/auth/tokens')
    hconf.set(prefix + ".auth.endpoint.prefix", "endpoints")
    hconf.set(prefix + ".tenant", credentials['projectId'])
    hconf.set(prefix + ".username", credentials['userId'])
    hconf.set(prefix + ".password", credentials['password'])
    hconf.setInt(prefix + ".http.port", 8080)
    hconf.set(prefix + ".region", credentials['region'])
    hconf.setBoolean(prefix + ".public", True)
