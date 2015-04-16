__author__ = 'sijialiu'

from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader('lab6_roster', 'templates'))
template = env.get_template('roster.html')

student_list = roster_101.lab6_roster.parse_roster.get_student_list()

table_str_list = []

str_html = template.render(title="Lab 6 Roster", student_list=student_list)

with open('lab6_html_roster_v4.html', 'w') as myFile:
    myFile.write(str_html)
    myFile.close()
    print "Done!"

