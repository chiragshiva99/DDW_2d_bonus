from flask_wtf import FlaskForm
from wtforms import FloatField, HiddenField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import MLRModel



#CHANGE THE FIELDS
class MLRForm(FlaskForm):
    hdi = FloatField('Human Development Index', validators=[DataRequired()])
    monthly_case = IntegerField('Monthly Cases', validators=[DataRequired()])
    pop_den = FloatField('Population Density', validators=[DataRequired()])
    death_count = HiddenField('Death Count')
    submit = SubmitField('Submit')

class LogRegForm(FlaskForm):
    mental_perc = FloatField('Mental Illness Percentage', validators=[DataRequired()])
    ff_per_hund = FloatField('# Fast food restaurants per 100 000 people', validators=[DataRequired()])
    hypert = FloatField('Hypertension Percentage', validators=[DataRequired()])
    is_high_risk = HiddenField('High Risk')
    submit = SubmitField('Submit')

    
