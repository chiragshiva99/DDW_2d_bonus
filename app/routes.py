from flask import render_template
from app import application
from app.forms import MLRForm
from app.models import MLRModel


@application.route('/')
@application.route('/home')
def home():
    return render_template('Home.html', title='D2W-Bonus-Home')


@application.route('/about')
def about():
    return render_template('About.html', title='D2W-Bonus-About')


@application.route('/task1', methods=['GET', 'POST'])
def task1():
    form = MLRForm()
    MLR = MLRModel(num_task=1)
    if form.validate_on_submit():
        pop_den = form.pop_den.data
        hdi = form.hdi.data
        med_age = form.med_age.data

        form.death_count = MLR.beta0 + MLR.beta1 * pop_den + MLR.beta2 * hdi + MLR.beta3 * med_age
        return render_template('Task-1.html', title='D2W-Bonus-Task1', form=form)
    return render_template('Task-1.html', title='D2W-Bonus-Task1', form=form)


@application.route('/task2', methods=['GET', 'POST'])
def task2():
    return render_template('Task-2.html', title='D2W-Bonus-Task2')




