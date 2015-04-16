__author__ = 'sijialiu'

from jinja2 import Environment, PackageLoader
from student import Student

env = Environment(loader=PackageLoader('roster_101', 'templates'))
template = env.get_template('roster.html')


def get_student_list():
    s_list = []

    import os

    print os.getcwd()

    print "Reading roster ..."
    f = open('roster_101/data/roster.txt', 'r')

    for line in f:
        stu = Student(line)
        stu.grade()
        s_list.append(stu)

    return s_list


student_list = get_student_list()

table_str_list = []

str_html = template.render(title="Lab 6 Roster", student_list=student_list)

with open('lab6_html_roster.html', 'w') as roster_html:
    roster_html.write(str_html)
    roster_html.close()
    print "Done!"

