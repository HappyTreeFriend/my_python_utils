#!/usr/bin/env python
#-*-coding:utf-8-*-
#Created by happytree on 28/3/17.
#Description: My HTTP Connection Library, supporting GET, POST, Cookie, Header

import httplib
import urllib
import urlparse
import time

class MyHTTP(object):
    """ My HTTP Connection Library, supporting GET, POST, Cookie, Header """

    def __init__(self, url, data="", cookie="", headers="", debug=False, need_format_data=True):
        """ Initialization Parameters """
        self.debug = debug
        self.url = url
        _dict_url = self._separate_url()
        self.scheme, self.host, self.port, self.path  \
            , self.query = _dict_url["scheme"], _dict_url["host"]  \
            , _dict_url["port"], _dict_url["path"], _dict_url["query"]
        self.headers = {}
        self.data = ""
        self.cookie = ""
        if self._check_input(headers):
            self.headers = self._format_headers(headers)
            self.headers.update(self.headers)
        elif self._check_input(cookie):
            self.cookie = self._format_headers(cookie)
            self.headers.update(self.cookie)
        if need_format_data and self._check_input(data):
            self.data = urllib.urlencode(self._format_data(data))  # urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
        elif not need_format_data:
            self.data = data
        self._connect()

    def _debug_print(self, message):
        """ Print Formatting """
        if self.debug:
            print " [*]  ", message

    def _separate_url(self):
        """ Formatting URL Parameter """

        dict_url = dict()

        tuple_url = urlparse.urlparse(self.url)
        dict_url["host"] = tuple_url.netloc.split(":")[0]
        dict_url["port"] = 80 if not tuple_url.port else tuple_url.port
        dict_url["scheme"] = tuple_url.scheme
        dict_url["path"] = tuple_url.path
        dict_url["query"] = tuple_url.query
        return dict_url

    def _connect(self):
        if httplib.HTTP_PORT == self.port:
            self._connect = httplib.HTTPConnection(host=self.host, port=self.port, timeout=10000)
        elif httplib.HTTPS_PORT == self.port:
            self._connect = httplib.HTTPSConnection(host=self.host, port=self.port, timeout=10000)

    def _check_input(self, input):
        if input and type({}) != type(input):  return True

    def http_get(self):
        #time.sleep(40)
        request = self._connect.request(url=self.url
                                        , headers=self.headers
                                        , body=self.data
                                        , method="GET")
        self._debug_print("GET> host: %s, port: %d" % (self.host, self.port))
        #self._debug_print("cookie: %s" % self.cookie)
        self._debug_print("data: %s" % self.data)
        response = self._connect.getresponse(request)
        self._debug_print("Response> code: %d, msg: %s" % (response.status, response.reason))

        return response.read()

    def http_post(self):
        #time.sleep(10)
        request = self._connect.request(url=self.url
                                        , headers=self.headers
                                        , body=self.data
                                        , method="POST")
        self._debug_print("POST> url: %s" % self.url)
        # self._debug_print("cookie: %s" % self.cookie)
        self._debug_print("data: %s" % self.data)
        response = self._connect.getresponse(request)
        self._debug_print("Response> code: %d, msg: %s" % (response.status, response.reason))

        return response.read()


    def _format_data(self, data):
        dict_data = dict()

        for seq in data.split("&"):
            key, value = seq.split("=")
            dict_data[key] = value

        return dict_data

    def _format_headers(self, data):
        dict_data = dict()

        for seq in data.split("\n"):
            key = seq.split(":")[0]
            value = "".join(seq.split(":")[1:])
            dict_data[key] = value

        return dict_data


class MyHTTPTest(object):
    def __init__(self):
        self.url = "https://www.baidu.com"
        self.cookie = "Cookie: a=1; b=2"

    def action(self):
        print "Start Test MYHTTP"

        my_http = MyHTTP(url=self.url, cookie=self.cookie, debug=True)
        print my_http.http_get()

if __name__ == "__main__":
    my_http_test = MyHTTPTest()
    my_http_test.action()