from flask import render_template
from app import application


@application.route('/')
@application.route('/home')
def home():
    return render_template('Home.html', title='D2W-Bonus-Home')


@application.route('/about')
def about():
    return render_template('About.html', title='D2W-Bonus-About')


@application.route('/task1')
def task1():
    return render_template('Task-1.html', title='D2W-Bonus-Task1')


@application.route('/task2')
def task2():
    return render_template('Task-2.html', title='D2W-Bonus-Task2')




