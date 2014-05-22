# coding=utf-8
__author__ = 'HuCC'

import sys
import httplib

T="6B811495D73B59E55DE9754529A0ED38"

if __name__ == "__main__":
    c=sys.argv[1]
    conn = httplib.HTTPConnection("127.0.0.1:1819")
    conn.request("GET", "/c?t="+T+"&c="+c)
    response = conn.getresponse()
    print response.read()