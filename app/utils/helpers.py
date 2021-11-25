from flask.helpers import flash
from wtforms.validators import ValidationError


def validate_hdi(hdi):
    if float(hdi) >= 1 or float(hdi) < 0.8499999999 :
        flash('Please choose a range from 0.85 to 0.99 for the Human Development Index')
        return False
    else: return True

def validate_monthly_case(monthly_case):
    if float(monthly_case) > 30000 or float(monthly_case) < 100 :
        flash('Please choose a range from 100 to 30,000 for the Monthly Case')
        return False
    else: return True

def validate_pop_den(pop_den):
    if float(pop_den) > 500 or float(pop_den) < 3 :
        flash('Please choose a range from 100 to 500 for the Population Density')
        return False
    else: return True