from flask_table import Table, Col , LinkCol

class Results(Table):
    id = Col('Id', show=True)
    first_name = Col('First name')
    last_name = Col('Last name')
    age = Col('Age')
    company = Col('Company')
    country = Col('Country')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))
 