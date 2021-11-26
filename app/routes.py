from flask import render_template, flash, redirect, url_for, request
from app import application
from app.forms import MLRForm, LogRegForm
from app.models import MLRModel, LogRegModel
from app.utils.helpers import validate_hdi, validate_monthly_case, validate_pop_den, validate_ff_per_hund, validate_hypert,validate_mental_perc, normalize_z


@application.route('/')
@application.route('/home')
def home():
    return render_template('Home.html', title='D2W-Bonus-Home')


@application.route('/about')
def about():
    return render_template('About.html', title='D2W-Bonus-About')



#filter data from the various boundaries 
@application.route('/task1', methods=['GET', 'POST'])
def task1():
    form = MLRForm()
    MLR = MLRModel()
    if form.validate_on_submit():
        pop_den = form.pop_den.data
        hdi = form.hdi.data
        monthly_case = form.monthly_case.data

        flag1 = validate_pop_den(pop_den)
        flag2 = validate_hdi(hdi)
        flag3 = validate_monthly_case(monthly_case)

        if not flag1 or not flag2 or not flag3:
            return render_template('Task-1.html', title='D2W-Bonus-Task1', form=form) ########
        
        if request.method == "POST":
            todo = request.form.get("todo")
            print(todo)

        form.death_count = MLR.beta0 + MLR.beta1 * pop_den + MLR.beta2 * hdi + MLR.beta3 * monthly_case
        return render_template('Task-1.html', title='D2W-Bonus-Task1', form=form) ##### 
    return render_template('Task-1.html', title='D2W-Bonus-Task1', form=form)


@application.route('/task2', methods=['GET', 'POST'])
def task2():
    form = LogRegForm()
    LRM =LogRegModel()
    if form.validate_on_submit():
        mental_perc = form.mental_perc.data
        ff_per_hund= form.ff_per_hund.data
        hypert = form.hypert.data

        flag1 = validate_mental_perc(mental_perc)
        flag2 = validate_ff_per_hund(ff_per_hund)
        flag3 = validate_hypert(hypert)

        mental_perc = normalize_z(mental_perc, feature_type='mental') 
        ff_per_hund = normalize_z(ff_per_hund, feature_type='ff')
        hypert = normalize_z(hypert, feature_type='hyp')

        if not flag1 or not flag2 or not flag3:
            return render_template('Task-2.html', title='D2W-Bonus-Task2', form=form)

        val = LRM.beta0 + LRM.beta1 * mental_perc + LRM.beta2 * ff_per_hund + LRM.beta3 * hypert
        form.is_high_risk = 'High risk' if val >= 60 else 'Low risk'
        
        return render_template('Task-2.html', title='D2W-Bonus-Task2', form=form)
    return render_template('Task-2.html', title='D2W-Bonus-Task2', form=form)




