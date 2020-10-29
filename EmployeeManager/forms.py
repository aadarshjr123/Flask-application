# forms.py

from wtforms import Form, StringField, SelectField

class EmployeeSearchForm(Form):
    choices = [('Name', 'Name'),
               ('Company', 'Company'),
               ('Country', 'Country')]
    select = SelectField('Search for employee:', choices=choices)
    search = StringField('')

class EmployeeForm(Form):

    
    first_name = StringField('first name')
    last_name = StringField('last name')
    age = StringField('age')
    company = StringField('company')
    country = StringField('country')
   