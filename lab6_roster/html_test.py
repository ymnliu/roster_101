__author__ = 'sijialiu'

import urllib2

try:
    response = urllib2.urlopen('http://www.acsu.buffalo.edu/~alexlenh/cse-101/')
    print response.info()['Last-Modified']
    html = response.read()
    # do something
    response.close()  # best practice to close the file
except urllib2.HTTPError:
    if response is not None:
        response.close()
