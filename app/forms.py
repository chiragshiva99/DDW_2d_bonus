from flask_wtf import FlaskForm
from wtforms import FloatField, HiddenField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo


class MLRForm(FlaskForm):
    hdi = FloatField('Human Development Index', validators=[DataRequired()])
    monthly_case = IntegerField('Monthly Cases', validators=[DataRequired()])
    pop_den = FloatField('Population Density', validators=[DataRequired()])
    death_count = HiddenField('Death Count')
    submit = SubmitField('Submit')


class LogRegForm(FlaskForm):
    mental_perc = FloatField('Mental Illness %', validators=[DataRequired()])
    ff_per_hund = FloatField('No. of Fast food restaurants per 100 000 people', validators=[DataRequired()])
    hypert = FloatField('Hypertension %', validators=[DataRequired()])
    is_high_risk = HiddenField('High Risk')
    submit = SubmitField('Submit')

    
