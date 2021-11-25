from flask.helpers import flash
from wtforms.validators import ValidationError


def validate_hdi(hdi):
    if float(hdi) >= 1 or float(hdi) < 0.5 :
        flash('Please choose a range from 0.5 to 0.99 for the Human Development Index')

def validate_monthly_case(monthly_case):
    if float(monthly_case) > 30000 or float(monthly_case) < 15 :
        flash('Please choose a range from 15 to 30,000 for the Monthly Case')

def validate_pop_den(pop_den):
    if float(pop_den) > 510 or float(pop_den) < 3 :
        flash('Please choose a range from 3 to 510 for the Population Density')