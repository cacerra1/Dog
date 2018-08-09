from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, InputRequired
from app.dogs.models import Dog, Vet, VetVisit, Doctor, Store, Purchase


class EditPurchase(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    unit_cost = IntegerField('Unit Cost', validators=[DataRequired()])
    total_cost = IntegerField('Total Cost', validators=[DataRequired()])
    date = DateField('Purchase Date', validators=[DataRequired()])
    submit = SubmitField('Enter')



def CreatePurchase():
    class TempForm(FlaskForm):
        item = StringField('Item', validators=[DataRequired()])
        quantity = IntegerField('Quantity', validators=[DataRequired()])
        unit_cost = IntegerField('Unit Cost', validators=[DataRequired()])
        total_cost = IntegerField('Total Cost', validators=[DataRequired()])
        date = DateField('Purchase Date', validators=[DataRequired()])
        #submit = SubmitField('Enter') #moved this own below
    choices = list()
    for store in Store.query.all():  # <- assumes store_id and store_names are unique
        choices.append((str(store.id), store.name))
    TempForm.store_id = SelectField("Store Selector", choices=choices, validators=[InputRequired()])
    TempForm.submit = SubmitField('Enter')
    return TempForm()



def CreateAppointment():
    class TempForm(FlaskForm):

        reason = StringField('Visit Reason', validators=[DataRequired()])
        cost = IntegerField('Total Cost', validators=[DataRequired()])
        date = DateField('Visit Date', validators=[DataRequired()])
        #submit = SubmitField('Enter') I had to move this down below

    choices_d = list()
    for dog in Dog.query.all():
        choices_d.append((str(dog.id), dog.name))
    TempForm.dog_id = SelectField("Dog", choices=choices_d, validators=[InputRequired()])

    choices_v = list()
    for vet in Vet.query.all():
        choices_v.append((str(vet.id), vet.name))
    TempForm.vet_id = SelectField("Vet", choices=choices_v, validators=[InputRequired()])
    TempForm.submit = SubmitField('Enter')
    return TempForm()


class EditAppointment(FlaskForm):
    reason = StringField('Visit Reason', validators=[DataRequired()])
    cost = IntegerField('Cost', validators=[DataRequired()])
    date = DateField('Purchase Date', validators=[DataRequired()])
    submit = SubmitField('Enter')





