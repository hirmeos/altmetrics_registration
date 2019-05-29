#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import base64
import httplib2

URI_API_USER = os.environ['URI_API_USER']
URI_API_PASS = os.environ['URI_API_PASS']
AUTH_API_ENDP = os.environ['AUTH_API_ENDP']
URI_API_WORKS = os.environ['URI_API_WORKS']
ALTMETRICS_AUTH_ENDP = os.environ['ALTMETRICS_AUTH_ENDP']
ALTMETRICS_ENDP = os.environ['ALTMETRICS_ENDP']
ALTMETRICS_USER = os.environ['ALTMETRICS_USER']
ALTMETRICS_PASS = os.environ['ALTMETRICS_PASS']


class IdentifiersClient(object):
    """Single entry point to the translation service API"""

    def __init__(self):
        self.token = self.get_token(AUTH_API_ENDP, URI_API_USER, URI_API_PASS)
        self.auth = 'Bearer ' + self.token
        self.auth_headers = {'Authorization': self.auth}

    def get_token(self, url, email, passwd):
        h = httplib2.Http()
        credentials = {'email': email, 'password': passwd}
        headers = {'content-type': 'application/json'}
        res, content = h.request(url, 'POST', json.dumps(credentials), headers)
        if res.status != 200:
            raise ValueError(content.decode('utf-8'))
        return json.loads(content.decode('utf-8'))['data'][0]['token']

    def request_identifiers(self, url):
        h = httplib2.Http()
        res, content = h.request(url, 'GET', headers=self.auth_headers)
        if res.status != 200:
            raise ValueError(content.decode('utf-8'))
        return json.loads(content.decode('utf-8'))['data']

    def get_all_works(self):
        url = (URI_API_WORKS
               + '?filter=uri_scheme:http,uri_scheme:https,uri_scheme:info:doi'
               + '&strict=true')
        return self.request_identifiers(url)


class AltmetricsClient(object):
    """Single entry point to the altmetrics API"""

    def __init__(self):
        self.token = self.get_token(ALTMETRICS_AUTH_ENDP, ALTMETRICS_USER,
                                    ALTMETRICS_PASS)
        self.auth = 'Bearer ' + self.token
        self.auth_headers = {'Authorization': self.auth}

    def get_token(self, url, email, passwd):
        h = httplib2.Http()
        auth = base64.b64encode(bytes('%s:%s' % (email, passwd), 'utf-8'))
        headers = {'Authorization': 'Basic %s' % (auth.decode('utf-8'))}
        res, content = h.request(url, 'GET', headers=headers)
        if res.status != 200:
            raise ValueError(content.decode('utf-8'))
        return content.decode('utf-8')

    def register_dois(self, data):
        h = httplib2.Http()
        headers = {**{'content-type': 'application/json'}, **self.auth_headers}
        res, content = h.request(ALTMETRICS_ENDP, 'POST', json.dumps(data),
                                 headers=headers)
        if res.status != 200:
            raise ValueError(content.decode('utf-8'))
        return json.loads(content.decode('utf-8'))
