# main.py
from app import app
from db_setup import init_db, db_session
from forms import EmployeeSearchForm,EmployeeForm
from flask import flash, render_template, request, redirect
from models import Details,Employee
from tables import Results
import pandas as pd

init_db()

@app.route('/', methods=['GET', 'POST'])

def index():
    search = EmployeeSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search)

@app.route('/results')

def search_results(search):
    results = []
    search_string = search.data['search']
    # artist = employee album = details
    if search_string:
        if search.data['select'] == 'Employee':
            qry = db_session.query(Details, Employee).filter(
                Employee.id==Details.employee_id).filter(
                    Employee.name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'Details':
            qry = db_session.query(Details).filter(
                Details.title.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Country':
            qry = db_session.query(Details).filter(
                Details.country.contains(search_string))
            results = qry.all()
        else:
            qry = db_session.query(Details)
            results = qry.all()
    else:
        qry = db_session.query(Details)
        results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)

@app.route('/new_employee', methods=['GET', 'POST'])

def new_employee():
   
    form = EmployeeForm(request.form)

    if request.method == 'POST' and form.validate():
        details = Details()
        save_changes(details, form, new=True)
        flash('Employee Details created successfully!')
        return redirect('/')

    return render_template('new_employee.html', form=form)

def save_changes(details, form, new=False):
   
    details.first_name = form.first_name.data
    details.last_name = form.last_name.data
    details.age = form.age.data
    details.company = form.company.data
    details.country = form.country.data
    if new:
        # Add the new album to the database
        db_session.add(details)
    # commit the data to the database
    db_session.commit()


@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Details).filter(
                Details.id==id)
    details = qry.first()

    if details:
        form = EmployeeForm(formdata=request.form, obj=details)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(details, form)
            flash('Employee Details updated successfully!')
            return redirect('/')
        return render_template('edit_details.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  
    qry = db_session.query(Details).filter(
        Details.id==id)
    details = qry.first()
    if details:
        form = EmployeeForm(formdata=request.form, obj=details)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db_session.delete(details)
            db_session.commit()
            flash('Employee Details deleted successfully!')
            return redirect('/')
        return render_template('delete_details.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)

# @app.route('/save/%3Cint:id%3E', methods=['GET', 'POST'])
def save(id):
    # if not results:
    #     flash('No results found!')
    #     return redirect('/')
    # else:
        url = "http://127.0.0.1:5000/"
        table = pd.read_html(url)[0]
        name ="dataname"
        table.to_excel("%s.xlsx" % name)
        print("Excel file has been created successfully!")

if __name__ == '__main__':
    app.run()
