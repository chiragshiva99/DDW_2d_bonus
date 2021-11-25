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

def validate_mental_perc(val):
    if float(val) >= 100 or float(val) < 1 :
        flash('Please choose a range from 1 to 100 for the Mental Illness Percentage')
        return False
    else: return True

def validate_ff_per_hund(val):
    if float(val) >= 100 or float(val) < 1 :
        flash('Please choose a range from 1 to 100 for the Number of Fast food restaurants per 100 000 people')
        return False
    else: return True

def validate_hypert(val):
    if float(val) >= 100 or float(val) < 1 :
        flash('Please choose a range from 1 to 100 for the Hypertension Percentage')
        return False
    else: return True

def normalize_z(val, feature_type):
    if feature_type == 'mental':
        mean = -6.204714e-16
        sd = 1.0
    if feature_type == 'ff':
        mean = 1.026061e-15
        sd = 1.0
    if feature_type == 'hyp':
        mean = -1.150812e-15
        sd = 1.0

    return (val - mean) / sd