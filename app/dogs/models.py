from app import db
from datetime import *

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    sex = db.Column(db.String(2))
    breed = db.Column(db.String(50))
    image_file = db.Column(db.String(200))
    adopt_date = db.Column(db.DateTime) # add date like this adopt_date='2015-04-01 00:00:00')
    birth_date = db.Column(db.DateTime)


    appointment = db.relationship('VetVisit', backref='dog', lazy='dynamic')

    # orders = db.relationship('Order', backref='member', lazy='dynamic') # you will not see this is postgress, only SQLAlchemy.
    # courses = db.relationship('Course', secondary= 'user_courses', backref='member', lazy='dynamic')
    # this backref of member adds the virutal column to the Course table

    def __repr__(self):
	    return f"Dog('{self.name}', '{self.breed}')"


class Vet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    phone = db.Column(db.Integer)
    fax = db.Column(db.Integer)
    address = db.Column(db.String(200))
    city = db.Column(db.String(60))
    state = db.Column(db.String(60))
    zip = db.Column(db.Integer)

    vet_visit = db.relationship('VetVisit', backref='vet', lazy='dynamic')

    def __repr__(self):
        return f"Vet: ('{self.name}', Phone: '{self.phone}')"


class VetVisit(db.Model):

    __tablename__ = 'vetvisit'
    __searchable__ = ['body']

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    reason = db.Column(db.String(200))
    cost = db.Column(db.Integer)
    dog_id = db.Column(db.Integer, db.ForeignKey('dog.id'))
    vet_id = db.Column(db.Integer, db.ForeignKey('vet.id'))

    doctor = db.relationship('Doctor', backref='vetvisit', lazy='dynamic')

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    specialty = db.Column(db.String(80))
    vet_id = db.Column(db.Integer, db.ForeignKey('vetvisit.id'))


    def __repr__(self):
        return f"Doctor's Name: ('{self.fname}', '{self.phone}')"


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    phone = db.Column(db.Integer)
    fax = db.Column(db.Integer)
    address = db.Column(db.String(200))
    city = db.Column(db.String(60))
    state = db.Column(db.String(60))
    zip = db.Column(db.Integer)

    orders = db.relationship('Purchase', backref='store', lazy='dynamic')


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(80))
    quantity = db.Column(db.Integer)
    unit_cost = db.Column(db.Integer)
    total_cost= db.Column(db.Integer)
    date = db.Column(db.DateTime)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))



