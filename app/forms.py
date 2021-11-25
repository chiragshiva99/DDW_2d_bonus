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

    
