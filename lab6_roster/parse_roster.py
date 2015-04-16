__author__ = 'sijialiu'
import urllib2
import datetime

import pytz
import dateutil.parser

from lab6_roster.student import Student


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
"""

print "Reading roster ..."
f = open('roster.txt', 'r')

student_list = []

for line in f:
    student_list.append(Student(line))

print "Generating html roster ..."

with open('lab6_html_roster_v2.html', 'w') as myFile:
    myFile.write('<html>')
    myFile.write('<body>')
    myFile.write('<h1> CSE 101 Lab 6 Roster</h1>')

    for student in student_list:
        submit_time = student.submit_time
        str_is_late = ""

        if submit_time is not None:
            if submit_time > due_date:
                str_is_late = "(Late: %s)" % submit_time.strftime(time_format)
            myFile.write("<p> <a href=\"%s\">%s (%s)</a> %s</p>\n" %
                         (student.lab6_url, student.full_name, student.ubit_name, str_is_late))
        else:
            submit_time_alt = student.submit_time_alt
            if submit_time_alt is not None:
                if submit_time_alt > due_date:
                    str_is_late = "(Late: %s)" % submit_time_alt.strftime(time_format)
                myFile.write("<p><a href=\"%s\">%s backup1 (%s)</a></p>\n" %
                             (student.lab6_url_alt, student.full_name, student.ubit_name))
            else:
                myFile.write("<p>%s (%s) Not submit \n" % (student.full_name, student.ubit_name))
                myFile.write(" <a href=\"%s\">%s</a> \n" % (student.lab6_url, student.full_name))
                myFile.write(", <a href=\"%s\">alt </a></p>\n" % student.lab6_url_alt)

    myFile.write('</body>')
    myFile.write('</html>')

    myFile.close()

print "Done"
"""


def get_student_list():
    s_list = []

    print "Reading roster ..."
    f = open('roster.txt', 'r')

    for line in f:
        stu = Student(line)
        stu.grade()
        s_list.append(stu)

    return s_list