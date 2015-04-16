__author__ = 'sijialiu'
import re
import urllib2
import dateutil
import datetime
import pytz
import re

due_date = datetime.datetime(2015, 4, 12, 23, 59, tzinfo=pytz.utc)
time_format = '%b %d %Y %H:%M'

contain_email = re.compile('mailto:[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}', re.I)
contain_email_quote = re.compile('mailto:\"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}\"', re.I)

contain_hr = re.compile('<hr', re.I)


def get_url_last_modified_datetime(url_str):
    response = None
    try:
        response = urllib2.urlopen(url_str)
        last_modified_date = response.info()['Last-Modified']
        submit_time = dateutil.parser.parse(last_modified_date)
        response.close()  # best practice to close the file
        return submit_time
    except urllib2.HTTPError:
        if response is not None:
            response.close()
        return None
    except KeyError:
        if response is not None:
            response.close()
        return due_date


class Student(object):
    line = ""
    str_is_late = ""
    submit_time = None
    submit_time_alt = None
    is_submitted = False
    is_submitted_alt = False
    is_late = False
    last_modified_str = ""
    status = ""

    def __init__(self, _line):
        self.line = _line
        self.ubit_name = self.get_ubit_name()
        self.full_name = self.get_full_name()
        self.lab6_url = "http://www.acsu.buffalo.edu/~%s/cse-101" % self.ubit_name
        self.lab6_url_alt = "http://www.acsu.buffalo.edu/~%s" % self.ubit_name


    def get_ubit_name(self):
        return re.compile("\((.*)\)").search(self.line).group(1)

    def get_full_name(self):
        try:
            return re.match("\w+,.([\w]+\s)+", self.line).group(0)
        except AttributeError:
            return None

    def grade(self):
        self.submit_time = get_url_last_modified_datetime(self.lab6_url)
        self.submit_time_alt = get_url_last_modified_datetime(self.lab6_url_alt)

        print "Grading %s" % self.full_name

        if self.submit_time is not None:
            self.is_submitted = True

            if self.submit_time > due_date:
                self.is_late = True
                self.last_modified_str = self.submit_time.strftime(time_format)
                self.status += "Late "

                self.status += self.grade_from_html(self.lab6_url)
        elif self.submit_time_alt is not None:
            self.is_submitted = True
            self.is_submitted_alt = True
            self.status += "Alt "
            if self.submit_time_alt > due_date:
                self.is_late = True
                self.last_modified_str = self.submit_time_alt.strftime(time_format)
                self.status += "Late "

            self.status += self.grade_from_html(self.lab6_url_alt)
        else:
            self.status = "NA"

        print self.status

    def grade_from_html(self, url_str):
        status = ""
        response = urllib2.urlopen(url_str)
        the_page = response.read()
        if contain_email.search(the_page) is None and contain_email_quote.search(the_page) is None:
            status += "NE "

        if contain_hr.search(the_page) is None:
            status += "NR "

        response.close()  # best practice to close the file
        return status

