from app import db

class Employee(db.Model):
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
class Details(db.Model):
    
    __tablename__ = "details"
    id = db.Column(db.Integer, primary_key=True)
    #title
    first_name = db.Column(db.String)
    #title
    last_name = db.Column(db.String)
    #release_date
    age = db.Column(db.String)
    #publisher
    company = db.Column(db.String)
    #publisher
    country = db.Column(db.String)
    #artist_id
    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"))
    #artist
 