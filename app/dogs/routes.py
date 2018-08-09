from app.dogs import main
from app import db
from app.dogs.models import Dog, Vet, VetVisit, Doctor, Store, Purchase
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.dogs.forms import EditPurchase, CreatePurchase, CreateAppointment, EditAppointment
from app.auth.models import User

from flask_login import login_required
from flask_sqlalchemy import SQLAlchemy



import datetime
from datetime import date

@main.route('/')
def display_home():

    return render_template('home.html')


@main.route('/vet')
def vet_visits():
    vet = VetVisit.query.join(Vet).join(Dog)

    results = VetVisit.query.all()  # I only need this for the total cost
    total = 0
    for x in results:
        if x.cost is not type(None):
            total = total + x.cost
    end_total = total

    return render_template('vet.html' , vet=vet, end_total=end_total)


@main.route('/dogs')
def dogs():
    dog = Dog.query.all()
    now = datetime.datetime.now()
    year = now.year

    return render_template('dogs.html', dog=dog, now=now, year=year)


@main.route('/dogs/max/')
def max():

    return render_template('max.html',)


@main.route('/dogs/henry/')
def henry():

    return render_template('henry.html',)


@main.route('/dogs/rosie/')
def rosie():
    return render_template('rosie.html', )

@main.route('/dogs/fred/')
def fred():
    return render_template('fred.html', )


@main.route('/dogs/jake/')
def jake():
    return render_template('jake.html', )


@main.route('/purchases', methods=['GET', 'POST'])
def purchases():
    results = Purchase.query.all() # I only need this for the total cost
    total = 0
    for x in results:
        total = total + x.total_cost
    end_total = total
    # the join that joins Store table to the Purchase table
    store = Purchase.query.join(Store)


    return render_template('purchases.html', results= results, end_total=end_total, store=store, )


admin_list = ['claudia.acerra@gmail.com']

@main.route('/enter_purchases', methods=['GET', 'POST'])
@login_required
def enter_purchase():
    form = CreatePurchase()

    if form.validate_on_submit():
        purchase = Purchase(item=form.item.data, quantity=form.quantity.data, unit_cost=form.unit_cost.data,
                    total_cost=form.total_cost.data, date=form.date.data,store_id=form.store_id.data)

        db.session.add(purchase)
        db.session.commit()
        flash('New purchase added successfully')
        return redirect(url_for('main.success'))
    return render_template('enter_purchases.html', form=form)


@main.route('/edit_purchases/<purchase_id>', methods=['GET', 'POST'])
@login_required
def edit_purchase(purchase_id):
    purchase = Purchase.query.get(purchase_id)
    form = EditPurchase(obj=purchase)
    if form.validate_on_submit():
        #form.populate_obj(purchase)
        purchase.item=form.item.data
        purchase.quantity=form.quantity.data
        purchase.unit_cost=form.unit_cost.data
        purchase.total_cost=form.total_cost.data
        purchase.date=form.date.data
        #purchase.store_id=form.store_id.data

        db.session.add(purchase)
        db.session.commit()
        flash('Purchase Edited successfully')
        return redirect(url_for('main.success'))
    return render_template('edit_purchases.html', form=form)


@main.route('/success')
def success():
    return render_template('success.html')


@main.route('/enter_vet', methods=['GET', 'POST'])
@login_required
def enter_vet():

    form = CreateAppointment()

    if form.validate_on_submit():
        vetVisit = VetVisit(date=form.date.data, dog_id=form.dog_id.data, cost=form.cost.data, reason=form.reason.data,
                    vet_id=form.vet_id.data )

        db.session.add(vetVisit)
        db.session.commit()
        flash('New appointment added successfully')
        return redirect(url_for('main.success_vet'))
    return render_template('enter_vet.html', form=form)

@main.route('/edit_vet/<vet_id>', methods=['GET', 'POST'])

@login_required
def edit_vet_visit(vet_id):
    vet_visit = VetVisit.query.get(vet_id)
    form = EditAppointment(obj=vet_visit)
    if form.validate_on_submit():
        form.populate_obj(vet_visit)
        vet_visit.reason=form.reason.data
        vet_visit.cost=form.cost.data

        vet_visit.date=form.date.data
        # vet_visit.vet_id= form.vet.data
        # vet_visit.dog_id = form.doggie.data


        db.session.add(vet_visit)
        db.session.commit()
        flash('Vet Visit Edited successfully')
        return redirect(url_for('main.success_vet'))
    return render_template('edit_vet.html', form=form)

@main.route('/cancel/<vet_id>', methods=['GET', 'POST'])
@login_required
def cancel_vet(vet_id):
    vet_visit = VetVisit.query.get(vet_id)  #query vet-Visit-id id from DB
    if request.method == 'POST':
        db.session.delete(vet_visit)
        db.session.commit()
        flash('book delete successfully')
        return redirect(url_for('main.vet_visits'))
    return render_template('cancel_vet.html', vet_visit=vet_visit, vet__id=vet_visit.id) # if not post request go to the delete page



@main.route('/success_vet')
def success_vet():
    return render_template('success_vet.html')