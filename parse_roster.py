__author__ = 'sijialiu'
import urllib2
import datetime

import pytz
import dateutil.parser


def get_url_last_modified_date(url_str):
    response = None
    try:
        response = urllib2.urlopen(url_str)
        last_modified_date = response.info()['Last-Modified']
        url_submit_time = dateutil.parser.parse(last_modified_date)
        response.close()  # best practice to close the file
        return url_submit_time
    except urllib2.HTTPError:
        if response is not None:
            response.close()
        return None
    except KeyError:
        if response is not None:
            response.close()
        return due_date


due_date = datetime.datetime(2015, 4, 12, 23, 59, tzinfo=pytz.utc)
time_format = '%b %d %Y %H:%M'


def get_student_list():


    return s_list